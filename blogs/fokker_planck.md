---
title: "Markov Processes and the Fokker-Planck Equation"
layout: default
---
# Markov Processes and the Fokker-Planck Equation

This document provides a formal derivation of the Fokker-Planck equation starting from Markov process semigroups and SDEs.

---

## 1. Markov Processes and Semigroups
Assume a **time-homogeneous Markov Process** ($M-p$) with a semigroup $\{P_{t}\}$. For a function $f: \mathbb{R}^{d} \rightarrow \mathbb{R}$, the semigroup action is defined by:

$(P_{t}f)(X_{s}) = E[f(X_{t+s}) | \mathcal{F}_{s}]$$ 

Taking the expectation on both sides yields:
$$E[(P_{t}f)(X_{s})] = E[f(X_{t+s})]$$ 
$$\int_{\mathbb{R}^{d}} (P_{t}f)(x)\mu_{s}(x)dx = \int f(x)\mu_{t+s}(x)dx$$ 

### Semigroup Properties
The claim is that $P_{t+s}f = P_{s}(P_{t}f)$. We can verify this via:
$$P_{t+s}f(X_{0}) = E[f(X_{t+s})|X_{0}]$$ 
$$= E[E[f(X_{t+s})|\mathcal{F}_{s}]|X_{0}] = E[(P_{t}f)(X_{s})|X_{0}] = P_{s}(P_{t}f)(X_{0})$$ 

By swapping the roles of $s$ and $t$, we see $P_{t+s}f(X_{0}) = P_{t}(P_{s}f)(X_{0})$.

---

## 2. The Infinitesimal Generator
Given the transition probability $p(X_{t}=y|X_{0}=x)$, the operator $P_{t}$ maps $f$ to $g$ where:
$$g(x) = \int f(u)p(X_{t}=u|x)du$$ 

The **infinitesimal generator** $\mathcal{L}$ is defined as:
$$\mathcal{L}f(x) := \lim_{t\rightarrow 0} \frac{P_{t}f(x) - f(x)}{t}$$ 

If the process is given by the SDE:
$$dX_{t} = u(X_{t}, t)dt + \sigma(X_{t}, t)dB_{t}$$

---

## 3. Deriving the Fokker-Planck Equation
To find $\mathcal{L}$ for this process, we use the "Physicist Way" by expanding the expectation:

$$P_{t+dt}f(X_{0}) = E[E[f(X_{t+dt})|\mathcal{F}_{t}]|X_{0}]$$ 

Using a Taylor expansion (Itô's Lemma intuition):
$$E[f(X_{t}) + \langle \nabla f(X_{t}), u(X_{t}, t) \rangle dt + \frac{1}{2}\sigma^{2}(X_{t}, t)\Delta f(X_{t})dt | X_{0}]$$ 
$$= P_{t}f(X_{0}) + dt \cdot E[\langle \nabla f, u \rangle + \frac{1}{2}\sigma^{2}\Delta f | X_{0}]$$ 

### Integrating by Parts
Taking the expectation (integrating against the density $\mu_{t}$):
$$\int_{\mathbb{R}^{d}} f(x)(\mu_{t+dt}(x) - \mu_{t}(x))dx = dt \int_{\mathbb{R}^{d}} (\langle \nabla f, u \rangle + \frac{1}{2}\sigma^{2}\Delta f)\mu_{t} dx$$ 

By applying multi-variable calculus and assuming the density "dies out" at the boundaries:
1. $\int \mu_{t} \langle \nabla f, u \rangle dx = -\int f \nabla \cdot (u \cdot \mu_{t}) dx$ 
2. $\int \sigma^{2} \mu_{t} \Delta f dx = \int f \Delta (\sigma^{2} \mu_{t}) dx$ 

Since this holds for all test functions $f$, we arrive at:

### The Fokker-Planck Equation
$$\frac{\partial \mu(x, t)}{\partial t} = -\nabla \cdot (u(x, t)\mu(x, t)) + \frac{1}{2} \sum \frac{\partial^{2}}{\partial x_{i}^{2}}(\sigma^{2}(x, t)\mu(x, t))$$ 

---

## 4. Special Case: Langevin Dynamics
For Langevin dynamics, we assume:
* $u(x, t) = -\nabla V(x)$ 
* $\sigma(x, t) = \sqrt{2}$ 

Substituting these into the Fokker-Planck equation:
$$\frac{\partial \mu(x, t)}{\partial t} = -\nabla \cdot (-\nabla V(x) \mu(x, t)) + \Delta \mu(x, t)$$ 
$$\frac{\partial \mu(x, t)}{\partial t} = \mu(x, t)\Delta V(x) + \langle \nabla V(x), \nabla \mu(x, t) \rangle + \Delta \mu(x, t)$$ 
