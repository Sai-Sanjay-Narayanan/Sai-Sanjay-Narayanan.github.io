from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out = Path("assets/blogs/cantelli_inequality")
out.mkdir(parents=True, exist_ok=True)

lam = 1
x = np.linspace(-5, 5, 500)

plt.figure(figsize=(5, 3.2))
plt.plot(x, x / lam, label=r"$x/\lambda$", linewidth=2)
plt.step(x, x >= lam, where="post", label=r"$\mathbf{1}\{x \geq \lambda\}$", linewidth=2)

ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_xticks([lam])
ax.set_xticklabels([r"$\lambda$"])
ax.set_yticks([])
ax.tick_params(axis="x", length=0)
ax.tick_params(axis="y", length=0)
plt.ylim(-5.1, 5.1)
plt.legend()
plt.tight_layout()

plt.savefig(out / "indicator-vs-linear.svg")

k = 2.5
t = x / lam
numerator = (
    (2 * k - 3 * k**2) * t
    + (3 * k**2 - 1) * t**2
    + (1 - 2 * k) * t**3
)
f = numerator / (k**2 * (1 - k) ** 2)

plt.figure(figsize=(5, 3.2))
plt.plot(x, f, label=rf"$f(x)$", linewidth=2)
plt.step(x, x >= lam, where="post", label=r"$\mathbf{1}\{x \geq \lambda\}$", linewidth=2)

ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_xticks([lam])
ax.set_xticklabels([r"$\lambda$"])
ax.set_yticks([])
ax.tick_params(axis="x", length=0)
ax.tick_params(axis="y", length=0)
plt.ylim(-5.1, 5.1)
plt.legend()
plt.tight_layout()

plt.savefig(out / "indicator-vs-cubic.svg")

mu = 2
quadratic = ((x - mu) / lam) ** 2
outside_interval = (x - mu >= lam) | (x - mu <= -lam)

plt.figure(figsize=(5, 3.2))
plt.plot(x, quadratic, label=r"$(x-\mu)^2/\lambda^2$", linewidth=2)
plt.step(
    x,
    outside_interval,
    where="post",
    label=r"$\mathbf{1}\{|x-\mu| \geq \lambda\}$",
    linewidth=2,
)

ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_xticks([mu - lam, mu, mu + lam])
ax.set_xticklabels([r"$\mu-\lambda$", r"$\mu$", r"$\mu+\lambda$"])
ax.set_yticks([])
ax.tick_params(axis="x", length=0)
ax.tick_params(axis="y", length=0)
plt.ylim(-0.2, 5.1)
plt.legend()
plt.tight_layout()

plt.savefig(out / "chebyshev_depiction.svg")

mu = 2
c = 1
quadratic = ((x - mu) / lam) ** 2
shifted_quadratic = ((x - mu + c) / (lam + c)) ** 2
right_tail = x >= mu + lam

plt.figure(figsize=(5.4, 3.2))
plt.plot(x, quadratic, label=r"$(x-\mu)^2/\lambda^2$", linewidth=2)
plt.plot(
    x,
    shifted_quadratic,
    label=r"$(x-\mu+c)^2/(\lambda+c)^2$",
    linewidth=2,
)
plt.step(
    x,
    right_tail,
    where="post",
    label=r"$\mathbf{1}\{x \geq \mu+\lambda\}$",
    linewidth=2,
)

ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_xticks([mu - c, mu, mu + lam])
ax.set_xticklabels([r"$\mu-c$", r"$\mu$", r"$\mu+\lambda$"])
ax.set_yticks([])
ax.tick_params(axis="x", length=0)
ax.tick_params(axis="y", length=0)
plt.ylim(-0.2, 5.1)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.3), frameon=False)
plt.tight_layout()

plt.savefig(out / "cantelli_intuition.svg", bbox_inches="tight")
