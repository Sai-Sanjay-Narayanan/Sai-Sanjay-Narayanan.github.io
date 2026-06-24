---
title: "Cantelli's Inequality (and a general recipe for deriving moment bounds for probabilities)"
layout: default
---

I recently came across a stronger version of Chebyshev's inequality (called Cantelli's inequality) for one sided tail bounds. But before I state what it is, I would like to share a general recipe for deriving such bounds to begin with.

The main principle is the following: suppose $f, g: \mathbb{R} \rightarrow \mathbb{R}$ are two functions, and suppose $A \subseteq \mathbb{R}$ such that $f(x) \geq g(x)$ for all $x \in A$. If $X$ is a random variable such that $X \in A$ almost surely, then we have $\mathbb{E}[ f(X) ] \geq \mathbb{E} [ g(X) ]$. Typically, $g$ is chosen to be an indicator function $1_B (x)$ where $B \subseteq A$, so that we get $ \mathbb{P}(B) \leq \mathbb{E} [ f(X) ]$.

We will illustrate this principle with some pictures. To start with, let $g(x) = 1(x \geq \lambda)$ for some $\lambda \geq 0$, and let $f(x) = x/\lambda$. Below is a plot showing both the functions:

![Comparison of x over lambda and indicator function](/assets/blogs/cantelli_inequality/indicator-vs-linear.svg)

As we can clearly see, $f(x) \geq g(x)$ for all $x \geq 0$. Thus, if $X$ is a non-negative random variable, we have $\mathbb{E}[ f(X) ] \geq \mathbb{E}[ g(X) ]$, which in this case gives the well known Markov's inequality:
$$\boxed{ \mathbb{P}(X \geq 0) \leq \frac{\mathbb{E}[X]}{\lambda} } $$

The picture based derivation is useful because not only does it allow us to generalize, it also gives us an intuition for how good the bound is. For instance, if most of the probability mass happens to lie on those $x$ where $f(x)$ is significantly larger than $g(x)$ (in the case of Markov, for very large $x$), then we expect that the resulting bound will not be very good.

To illustrate another example involving third moments, suppose $X$ is a non-negative random variable with finite third moment. We would like to get a _lower_ bound on $P(X \geq \lambda)$ for some $\lambda \geq 0$, and this lower bound should involve $\mathbb{E}[ X^3]$ somehow.

As before, we let $g(x) = 1(x \geq \lambda)$, and this time we let $f(x)$ be a _cubic_ polynomial in $x$, with the property that $f(x) \leq g(x)$ for all $x \geq 0$. Here is such a picture:

![Comparison of the indicator function and cubic polynomial](/assets/blogs/cantelli_inequality/indicator-vs-cubic.svg)

The question now is: how do we come up with such a cubic polynomial? Here we have a couple of design choices. Firstly, we may demand that $f(0) = f(\lambda) = 0$ (as seen in the picture). Now, the local maximum of $f$ must occur at $x = \alpha \lambda$ where $\alpha > 1$, and we may demand that $f(\alpha \lambda) = 1$ (also seen in the picture). This gives us a family of cubic polynomials (parameterized by $\alpha$). The interested reader may refer to [this](https://www.pp.bme.hu/ci/article/view/3862) paper for the precise formula for such a cubic.

## Cantelli's Inequality

We now return to the original subject, namely Cantelli's inequality. This is often motivated as a tighter version for Chebyshev's inequality for one-sided tail bounds. So, we must first understand Chebyshev's inequality.

Chebyshev's inequality gives us an upper bound for $\mathbb{P}(\mid X - \mu \mid \geq \lambda)$, where $\mu = \mathbb{E}[X]$ , using second moments. By simply applying Markov's inequality to the non-negative random variable $(X - \mu)^2$, we get the upper bound $\frac{\text{Var}(X)}{\lambda^2}$ (note that $\text{Var}(X) = \mathbb{E}[ (X - \mu)^2 ]$). However, we get a little more insight using the picture based derivation:

![Chebyshev inequality depiction](/assets/blogs/cantelli_inequality/chebyshev_depiction.svg)

In particular, we observe that the quadratic $f(x) = (x - \mu)^2 / \lambda^2 $ upper bounds _both_ the tails $1(x - \mu \geq \lambda)$ and $1(x - \mu \leq -\lambda)$, which is what allows us to get the required upper bound for $\mathbb{P}(\mid X - \mu \mid \geq \lambda)$. Obviously, Chebshev's upper bound is also an upper bound for each of the individual tail probabilities $\mathbb{P}(X - \mu \geq \lambda)$ and $\mathbb{P}(X - \mu \leq -\lambda)$.

Now we ask: what if I am not interested in upper bounding both the tail probabilities? What if I want to just upper bound the right tail, i.e. $\mathbb{P}(X - \mu \geq \lambda)$? Is there a better upper bound involving second moment? It turns out the answer is yes, and this is the content of Cantelli's inequality.

Let us first try to get an intuition for why we may expect a better upper bound for the single tail. The key insight that  $f(x) = (x - \mu)^2 / \lambda^2 $ is _not_ the only quadratic that upper bounds the right tail, as seen in the following picture:

![Cantelli intuition plot](/assets/blogs/cantelli_inequality/cantelli_intuition.svg)

Here, the blue curve is the quadratic used to obtain Chebyshev's bound, while the orange curve is a quadratic whose zero point is shifted from $\mu$ to $\mu - c$ for some positive $c$. Why might we expect the orange curve to result in a better bound? Intuitively, if the variance of $X$ is large, then the probability mass extends a lot in the right tail, and so we want the quadratic to not be so "steep" to give us a tighter bound. In fact, by extending this logic, we would expect the optimal shift $c$ to increase as the variance increases.

We will now work out the fairly simple algebra to compute the optimal shift $c$ for a given random variable $X$ with finite variance $V := \text{Var}(X)$. Letting $f(x) = \frac{(x - \mu + c)^2}{(\lambda + c)^2}$ for some $c > -\lambda$ and noting that $f(x) \geq 1(x \geq \mu + \lambda)$, we obtain

$$\begin{align}
\mathbb{P}(X \geq \mu + \lambda) \leq \frac{\mathbb{E}[(X - \mu + c)^2]}{(\lambda + c)^2} = \frac{V + c^2}{(\lambda + c)^2}.
\end{align}$$

Denoting the RHS as $\phi(c)$, we want to find the $c > -\lambda$ that minimizes $\phi(c)$ to get the tightest possible bound. We compute

$$ \begin{align}
\phi'(c) &= \frac{(\lambda + c)^2 \cdot 2c - (V + c^2) \cdot 2(\lambda + c) }{(\lambda + c)^4} \\
&= \frac{2(\lambda c - V)}{(\lambda + c)^3}
\end{align}
$$

Clearly, $\phi'(c)=0$ when $c = \frac{V}{\lambda}$, and since the denominator $(\lambda + c)^3 > 0$ for all $c > -\lambda$ and the numerator is linear and increasing in $c$, we conclude that $c = \frac{V}{\lambda}$ corresponds to a local (and in this case, global) minimum for $\phi(c)$. We remark that the optimal $c$ matches our previous intuition: higher the variance, the larger the shift in the quadratic must be.

Finally, substituting this $c$ into the upper bound gives us Cantelli's inequality:

$$\boxed{\begin{align}
\mathbb{P}(X \geq \mu + \lambda) &= \frac{V}{V + \lambda^2}
\end{align}}$$
