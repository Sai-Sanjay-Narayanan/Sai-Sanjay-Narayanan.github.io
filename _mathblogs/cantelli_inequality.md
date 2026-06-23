---
title: "Cantelli's Inequality (and a general recipe for deriving moment bounds for probabilities)"
layout: default
---

I recently came across a stronger version of Chebyshev's inequality (called Cantelli's inequality) for one sided tail bounds. But before I state what it is, I would like to share a general recipe for deriving such bounds.

The main principle is the following: suppose $f, g: \mathbb{R} \rightarrow \mathbb{R}$ are two functions, and suppose $A \subseteq \mathbb{R}$. If $X$ is a random variable such that $X \in A$ almost surely, then we have $\mathbb{E}[ f(X) ] \geq \mathbb{E} [ g(X) ]$.