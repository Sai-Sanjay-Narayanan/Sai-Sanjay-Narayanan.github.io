---
title: "Cantelli's Inequality (and a general recipe for deriving moment bounds for probabilities)"
layout: default
---

I recently came across a stronger version of Chebyshev's inequality (called Cantelli's inequality) for one sided tail bounds. But before I state what it is, I would like to share a general recipe for deriving such bounds to begin with.

The main principle is the following: suppose $f, g: \mathbb{R} \rightarrow \mathbb{R}$ are two functions, and suppose $A \subseteq \mathbb{R}$ such that $f(x) \geq g(x)$ for all $x \in A$. If $X$ is a random variable such that $X \in A$ almost surely, then we have $\mathbb{E}[ f(X) ] \geq \mathbb{E} [ g(X) ]$. Typically, $g$ is chosen to be an indicator function $1_B (x)$ where $B \subseteq A$, so that we get $ \mathbb{P}(B) \leq \mathbb{E} [ f(X) ]$.

We will illustrate this principle with some pictures. To start with, let $g(x) = 1(x \geq \lambda)$ for some $\lambda \geq 0$, and let $f(x) = x/\lambda$. Below is a plot showing both the functions:

![Comparison of x over lambda and indicator function](/assets/blogs/cantelli_inequality/indicator-vs-linear.svg)

As we can clearly see, $f(x) \geq g(x)$ for all $x \geq 0$. Thus, if $X$ is a non-negative random variable, we have $\mathbb{E}[ f(X) ] \geq \mathbb{E}[ g(X) ]$, which in this case gives the well known Markov's inequality:
$$\boxed{ \mathcal{P}(X \geq 0) \leq \frac{\mathbb{E}[X]}{\lambda} } $$

The picture based derivation is useful because not only does it allow us to generalize, it also gives us an intuition for how good the bound is. For instance, if most of the probability mass happens to lie on those $x$ where $f(x)$ is significantly larger than $g(x)$ (in the case of Markov, for very large $x$), then we expect that the resulting bound will not be very good.

To illustrate another example involving third moments, suppose $X$ is a non-negative random variable with finite third moment. We would like to get a _lower_ bound on $P(X \geq \lambda)$ for some $\lambda \geq 0$, and this lower bound should involve $\mathbb{E}[ X^3]$ somehow.

As before, we let $g(x) = 1(x \geq \lambda)$, and this time we let $f(x)$ be a _cubic_ polynomial in $x$, with the property that $f(x) \leq g(x)$ for all $x \geq 0$. Here is such a picture:

![Comparison of the indicator function and cubic polynomial](/assets/blogs/cantelli_inequality/indicator-vs-cubic.svg)

The question now is: how do we come up with such a cubic polynomial? Here we have a couple of design choices. Firstly, we may demand that $f(0) = f(\lambda) = 0$ (as seen in the picture). Now, the local maximum of $f$ must occur at $x = \alpha \lambda$ where $\alpha > 1$, and we may demand that $f(\alpha \lambda) = 1$ (also seen in the picture). This gives us a family of cubic polynomials (parameterized by $\alpha$). The interested reader may refer to [this](https://www.pp.bme.hu/ci/article/view/3862) paper for the precise formula for such a cubic.

## Cantelli's Inequality



