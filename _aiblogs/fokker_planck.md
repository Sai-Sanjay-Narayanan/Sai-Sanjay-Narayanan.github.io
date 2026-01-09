---
title: "Non-rigorous derivation of Fokker-Planck Equation for SDE"
layout: default
---
# Markov Processes and the Fokker-Planck Equation

This post contains a non-rigorous derivation of the Fokker-Planck equation for a SDE (with a lot of skipped steps), mostly for my own reference. I had scribbled the derivation in my rough note, uploaded the images to Gemini 3 Pro and asked it to convert it to a markdown file. The end result is actually quite decent (after I made some corrections).

---

## 1. Markov Processes and Semigroups
Assume a time-homogeneous Markov Process with a semigroup $\{P_{t}\}$. For a function $f: \mathbb{R}^{d} \rightarrow \mathbb{R}$, the semigroup action is defined by:

$$(P_{t}f)(X_{s}) = E[f(X_{t+s}) | \mathcal{F}_{s}] = E[f(X_{t+s}) \mid X_s]$$ 

Taking the expectation on both sides yields:

$$\begin{align}
&E[(P_{t}f)(X_{s})] = E[f(X_{t+s})] \\
\implies &\int_{\mathbb{R}^{d}} (P_{t}f)(x)\mu_{s}(x)dx = \int f(x)\mu_{t+s}(x)dx
\end{align}
$$

### Semigroup Properties
The claim is that $P_{t+s}f = P_{s}(P_{t}f)$. We can verify this via:

$$ \begin{align}
P_{t+s}f(X_{0}) &= E[f(X_{t+s})|X_{0}] \\
 &= E[E[f(X_{t+s})|\mathcal{F}_{s}]|X_{0}] \\
 &= E[(P_{t}f)(X_{s})|X_{0}] = P_{s}(P_{t}f)(X_{0}).
\end{align}
$$

By swapping the roles of $s$ and $t$, we see $P_{t+s}f(X_{0}) = P_{t}(P_{s}f)(X_{0})$.

---

## 2. The Infinitesimal Generator
Given the transition probability $p(X_{t}=y|X_{0}=x)$, the operator $P_{t}$ maps $f$ to $g$ where:
$$g(x) = \int f(u)p(X_{t}=u|x)du$$ 

The **infinitesimal generator** $\mathcal{L}$ is defined as:
$$\mathcal{L}f(x) := \lim_{t\rightarrow 0} \frac{P_{t}f(x) - f(x)}{t}$$ 

---

## 3. Deriving the Fokker-Planck Equation

Suppose the Markov Process is given by the SDE $$dX_{t} = u(X_{t}, t)dt + \sigma(X_{t}, t)dB_{t}$$.

To find $\mathcal{L}$ for this process, we use the "Physicist Way" by expanding the expectation:

$$P_{t+dt}f(X_{0}) = E[ f(X_{t+dt} \mid X_0)] = E[E[f(X_{t+dt})|\mathcal{F}_{t}]|X_{0}] = E[E[f(X_{t+dt})| X_t ]|X_{0}].$$ 

Using a Taylor expansion (can be formalized using Itô's Lemma), we have:

$$\begin{align}
    E[f(X_{t+dt})| X_t ] = f(X_{t}) + \langle \nabla f(X_{t}), u(X_{t}, t) \rangle dt + \frac{1}{2}\sigma^{2}(X_{t}, t)\Delta f(X_{t})dt
\end{align}
$$

and hence

$$\begin{align}
P_{t+dt}f(X_{0}) &= E[f(X_{t}) + \langle \nabla f(X_{t}), u(X_{t}, t) \rangle dt + \frac{1}{2}\sigma^{2}(X_{t}, t)\Delta f(X_{t})dt | X_{0}] \\
&= P_{t}f(X_{0}) + dt \cdot E[\langle \nabla f, u \rangle + \frac{1}{2}\sigma^{2}\Delta f | X_{0}]
\end{align}
$$

$$\implies P_{t+dt}f(X_{0}) - P_{t}f(X_{0}) =  dt \cdot E[\langle \nabla f, u \rangle + \frac{1}{2}\sigma^{2}\Delta f | X_{0}]$$

Taking the expectation on both sides (integrating against the density $\mu_{t}$):
$$\int_{\mathbb{R}^{d}} f(x)(\mu_{t+dt}(x) - \mu_{t}(x))dx = dt \int_{\mathbb{R}^{d}} (\langle \nabla f, u \rangle + \frac{1}{2}\sigma^{2}\Delta f)\mu_{t} dx$$ 

By applying multi-variable calculus and assuming the density "dies out" at the boundaries, we obtain the following results (derivation skipped for now, will add later):
1. $\int \mu_{t} \langle \nabla f, u \rangle dx = -\int f \nabla \cdot (u \cdot \mu_{t}) dx$ 
2. $\int \sigma^{2} \mu_{t} \Delta f dx = \int f \Delta (\sigma^{2} \mu_{t}) dx$ 

Since this holds for all test functions $f$, we arrive at:

### The Fokker-Planck Equation
$$\frac{\partial \mu(x, t)}{\partial t} = -\nabla \cdot (u(x, t)\mu(x, t)) + \frac{1}{2} \sum \frac{\partial^{2}}{\partial x_{i}^{2}}(\sigma^{2}(x, t)\mu(x, t))$$ 

---

## 4. Special Case: Langevin Dynamics
For Langevin dynamics, we have assume:
* $u(x, t) = -\nabla V(x)$ 
* $\sigma(x, t) = \sqrt{2}$ 

Substituting these into the Fokker-Planck equation:
$$\frac{\partial \mu(x, t)}{\partial t} = -\nabla \cdot (-\nabla V(x) \mu(x, t)) + \Delta \mu(x, t)$$ 

$$\implies \boxed{\frac{\partial \mu(x, t)}{\partial t} = \mu(x, t)\Delta V(x) + \langle \nabla V(x), \nabla \mu(x, t) \rangle + \Delta \mu(x, t) }$$ 
