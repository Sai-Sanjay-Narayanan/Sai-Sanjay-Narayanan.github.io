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