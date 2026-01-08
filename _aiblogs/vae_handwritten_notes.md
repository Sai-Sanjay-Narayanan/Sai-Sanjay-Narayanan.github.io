---
title: "VAE Notes"
layout: default
---
# Latent Generative Models

The goal is to sample $x$ from a distribution $$p(x)$$ which we don't know, but we have access to a dataset $\{x_{1}, x_{2}, \cdots x_{N}\}$, where each $x_{i}$ is sampled independently from $p(x)$.

One way of doing this is to first sample $z$ from a known distribution $r(z)$ (say, a standard Gaussian), and then sample $x \sim p_{\theta}(x\mid z)$, where $p_{\theta}$ is a learned network; and ideally

$$p(x) = p_{\theta}(x) := \mathbb{E}_{z \sim r(z)} \left[ p_{\theta}(x\mid z) \right]$$

The standard way to learn such a network is to maximize the expected log-likelihood $\mathcal{L}(\theta)$, where

$$\mathcal{L}(\theta) = \mathbb{E}_{x \sim p(x)} \left[ \log p_{\theta}(x) \right].$$

(in practice, we use the empirical log-likelihood $\frac{1}{N} \sum_{i=1}^{N} \log p_{\theta}(x_{i})$)

Now, computing $p_{\theta}(x) = \int p_{\theta}(x\mid z) r(z) dz$ is in general intractable, and

can only be estimated using Monte-Carlo integration:

$$p_{\theta}(x) \approx \frac{1}{M} \sum_{i=1}^{M} p_{\theta}(x\mid z_{i}), \quad z_{i} \sim r(z)$$

One might think of using the above Monte-Carlo estimate for each $x_i$ in the training set, and then maximize the (estimated) empirical log-likelihood. But, this approach is wrong because if $\hat{p}_\theta(x)$ is the Monte-Carlo estimate of $p_\theta(x)$, then indeed 

$$\mathbb{E}_{z_i} [\hat{p}_\theta(x)] = p_\theta(x),$$

but 

$$\mathbb{E}_{z_i} \left[ \log \hat{p}_\theta(x) \right] \neq \log p_\theta(x),$$

i.e. $\log \hat{p}_\theta(x)$ is not an unbiased estimate of $\log p_\theta(x)$. (in fact, by Jensen's inequality we have 

$$\mathbb{E}_{z_i} \left[ \log \hat{p}_\theta(x) \right] \leq \log p_\theta(x);$$

this also foreshadows the upcoming trick:)

∴ The alternate approach is to consider a lower bound on $\log p_{\theta}(x)$:

$$\log p_{\theta}(x)$$

$$= \log \mathbb{E}_{z \sim r(z)} \left[ p_{\theta}(x\mid z) \right]$$

$$\geq \mathbb{E}_{z \sim r(z)} \left[ \log p_{\theta}(x\mid z) \right] \text{(from Jensen's Inequality)}$$


and hence,

$$\mathcal{L}(\theta) = \mathbb{E}_{x \sim p(x)} \left[ \log p_{\theta}(x) \right]$$

$$\geq \mathbb{E}_{x \sim p(x), z \sim r(z)} \left[ \log p_{\theta}(x\mid z) \right],$$

and so one might think of maximizing the lower bound

instead of $\mathcal{L}(\theta)$.

This looks nice, but it is actually not good. To see why, let us take a concrete example: Suppose $p_{\theta}(x\mid z)$ is modelled as a normal distribution $\mathcal{N}(\mu_{\theta}(z), \sigma^2 \mathcal{I})$. Then,

$$\log p_{\theta}(x\mid z) \propto -\|x - \mu_{\theta}(z)\|^2$$

and hence maximizing the lower bound is equivalent to minimizing $$\mathbb{E}_{x,z} \left[ \|x - \mu_{\theta}(z)\|^2 \right]$$

and since $x$ and $z$ are sampled independently, the optimal solution is given by $\mu_{\theta}(z) = \mathbb{E}[x] \quad \forall z$. In other words, the model simply learns the expected value $\mathbb{E}[x]$ and samples from $\mathcal{N}(\mathbb{E}[x], \sigma^2 \mathcal{I})$, which could be vastly different from the actual distribution $p(\cdot)$.

Example:

[Diagram showing two distributions - red labeled "Actual" and purple labeled "Learned" with different bimodal shapes]

So, what other option is there? It turns out that we can apply a clever trick:

$$p_{\theta}(x) = \int p_{\theta}(x\mid z) r(z) dz$$

$$= \int p_{\theta}(x\mid z) \cdot \frac{r(z)}{q_{\phi}(z\mid x)} \cdot q_{\phi}(z\mid x) dz,$$

where $q_{\phi}(z\mid x)$ is another distribution parameterized by $\phi$. Thus,

$$p_{\theta}(x) = \mathbb{E}_{z \sim q_{\phi}(z\mid x)} \left[ p_{\theta}(x\mid z) \frac{r(z)}{q_{\phi}(z\mid x)} \right],$$

and by Jensen,

$$\log p_{\theta}(x)$$

$$\geq \mathbb{E}_{z \sim q_{\phi}(z\mid x)} \left[ \log p_{\theta}(x\mid z) + \log \frac{r(z)}{q_{\phi}(z\mid x)} \right],$$

and hence

$$\mathcal{L}(\theta) \geq \mathbb{E}_{x,z} \left[ \log p_{\theta}(x\mid z) \right]$$

$$- \mathbb{E}_{x} \left[ \mathbb{D}_{KL} \left( q_{\phi}(\cdot\mid x) \| r(\cdot) \right) \right]$$

where $(x, z) \sim p(x) q_{\phi}(z\mid x)$, i.e. they are no longer independently sampled. We can now maximize the RHS over $(\theta, \phi)$, and this is strictly better than the previous approach (indeed, if the space of all $q_{\phi}$ is rich enough, then it presumably

contains $r(\cdot)$ as well.)

We now analyze the two terms present in the lower bound, and see what maximizing each of them individually achieves, with an example.

The first term is

$$\mathbb{E}_{x,z} \left[ \log p_{\theta}(x\mid z) \right]$$

$$\propto \mathbb{E}_{x,z} \left[ -\|x - \mu_{\theta}(z)\|^2 \right]$$

Now, if we parameterize $q_{\phi}(z\mid x)$ as $\mathcal{N}(\lambda_{\phi}(x), \Delta^2 \mathcal{I})$, then

we may write

$$z = \lambda_{\phi}(x) + \Delta \varepsilon$$

where $\varepsilon \sim \mathcal{N}(0, \mathcal{I})$ is independent of $x$.

∴ We want to minimize

$$\mathbb{E}_{x,\varepsilon} \left[ \|x - \mu_{\theta}(\lambda_{\phi}(x) + \Delta \varepsilon)\|^2 \right]$$

where $x \perp\!\!\!\perp \varepsilon$.

If we take the extreme example of $\Delta = 0$, then the optimal $(\theta, \phi)$ would satisfy

$$\mu_{\theta}(\lambda_{\phi}(x)) = x \quad \forall x,$$

i.e. if we think of $\lambda_{\phi}$ as the "encoder" (i.e. maps $x$ to latent $z$), and $\mu_{\theta}$ as the decoder (i.e. maps latent $z$ to $x$), then optimizing the first term alone would yield a latent that, in some sense, has the same dimensionality as $x$ (∵ $x$ and $z$ would have a one-one mapping).

The second term is

$$-\mathbb{E}_{x} \left[ \mathbb{D}_{KL} \left( q_{\phi}(\cdot\mid x) \| r(\cdot) \right) \right]$$

$$= -\mathbb{E}_{x} \left[ \mathbb{D}_{KL} \left( \mathcal{N}(\lambda_{\phi}(x), \Delta^2) \| \mathcal{N}(0, \mathcal{I}) \right) \right]$$

$$= -\mathbb{E}_{x} \left[ \lambda_{\phi}(x)^2 + \left( \begin{array}{c} \text{other terms} \\ \text{not involving} \\ \phi \end{array} \right) \right]$$

and thus maximizing this yields $\lambda_{\phi}(x) = 0 \quad \forall x$, i.e. if we take the extreme example $\Delta = 0$, then the encoder sends every $x$ to $z = 0$, i.e., maximal compression; and dimension of latent is zero.

This is obviously not compatible with the first term. So, minimizing the entire lower bound yields a solution $(\theta, \phi)$ that strikes a balance between keeping the latent space large enough that one doesn't lose too much information in encoding, while also compressing the latent space enough so that $q_{\phi}(\cdot\mid x)$ approximates $r(\cdot)$ for every $x$. This is the "variational autoencoder".