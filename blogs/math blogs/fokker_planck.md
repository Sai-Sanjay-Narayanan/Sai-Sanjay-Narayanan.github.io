# Markov Processes and the Fokker-Planck Equation

This document provides a formal derivation of the Fokker-Planck equation starting from Markov process semigroups and SDEs.

---

## 1. Markov Processes and Semigroups
Assume a **time-homogeneous Markov Process** ($M-p$) with a semigroup $\{P_{t}\}$. For a function $f: \mathbb{R}^{d} \rightarrow \mathbb{R}$, the semigroup action is defined by:

$$(P_{t}f)(X_{s}) = E[f(X_{t+s}) | \mathcal{F}_{s}]$$

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
$$ = P_{t}f(X_{0}) + dt \cdot E[\langle \nabla f, u \rangle + \frac{