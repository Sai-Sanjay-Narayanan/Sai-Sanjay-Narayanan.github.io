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
