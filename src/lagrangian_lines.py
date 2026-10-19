"""
EN3330 Assignment 03 - Question 3(b)
Lagrangian lines L(mu, x) for fixed x = 0, 1, 2, their lower envelope,
and the true dual function d(mu) = mu - mu^2/4.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

PLOTS_DIR = Path(__file__).resolve().parent.parent / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

# --- serif styling to match the LaTeX report -------------------------------
plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "font.size": 12,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "legend.fontsize": 11,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
})

MU_MAX = 4.5
mu = np.linspace(0.0, MU_MAX, 1000)

# L(mu, x) = x^2 + mu(1 - x)  ->  slope (1 - x), intercept x^2
lines = {
    0: (mu,            r"$L(\mu,0)=\mu$",      "tab:blue"),
    1: (np.ones_like(mu), r"$L(\mu,1)=1$",     "tab:green"),
    2: (4.0 - mu,      r"$L(\mu,2)=4-\mu$",    "tab:orange"),
}

envelope = np.min(np.vstack([v[0] for v in lines.values()]), axis=0)
d_true = mu - mu**2 / 4.0          # true dual function

fig, ax = plt.subplots(figsize=(8, 5))

# the three Lagrangian lines
for y, label, colour in lines.values():
    ax.plot(mu, y, "--", lw=1.4, color=colour, label=label, alpha=0.9)

# lower envelope of the three lines (the approximation)
ax.plot(mu, envelope, "-", lw=3.0, color="crimson", zorder=4,
        label=r"Lower envelope of the 3 lines")

# true dual function
ax.plot(mu, d_true, "-.", lw=2.0, color="black", zorder=3,
        label=r"True dual $d(\mu)=\mu-\frac{\mu^{2}}{4}$")

# tangency points: envelope touches d(mu) where the chosen x is the true
# minimiser x*(mu) = mu/2, i.e. x = 0 -> mu = 0, x = 1 -> mu = 2, x = 2 -> mu = 4
touch_mu = np.array([0.0, 2.0, 4.0])
touch_d = touch_mu - touch_mu**2 / 4.0
ax.plot(touch_mu, touch_d, "o", ms=8, mfc="white", mec="black",
        mew=1.8, zorder=6, label="Envelope touches $d(\\mu)$")

# per-point label offsets so none of them collide with the curves
offsets = {0.0: (10, -20), 2.0: (0, 14), 4.0: (8, 14)}
for m, d in zip(touch_mu, touch_d):
    ax.annotate(rf"$\mu={m:.0f}$", xy=(m, d), xytext=offsets[m],
                textcoords="offset points", fontsize=10,
                ha="center" if m == 2.0 else "left")

ax.axhline(0, color="black", lw=0.8)
ax.axvline(0, color="black", lw=0.8)

ax.set_xlabel(r"Dual variable $\mu$")
ax.set_ylabel(r"$L(\mu,x)$ and $d(\mu)$")
ax.set_title(r"Lagrangian lines, their lower envelope, and the true dual function")

ax.set_xlim(0, MU_MAX)
ax.set_ylim(-0.8, 4.4)
ax.set_xticks(np.arange(0, MU_MAX + 0.5, 0.5))
ax.grid(True, ls=":", lw=0.7, alpha=0.6)

# legend outside the data so it does not sit on top of the curves
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13),
          ncol=3, frameon=False)

fig.tight_layout()
fig.savefig(PLOTS_DIR / "lagrangian_lower_envelope.png", dpi=300, bbox_inches="tight")
print("saved lagrangian_lower_envelope.png")

# --- numerical check that the envelope never dips below the true dual ------
assert np.all(envelope >= d_true - 1e-12), "envelope dips below d(mu)"
for m in touch_mu:
    e = min(m, 1.0, 4.0 - m)
    print(f"mu={m:.0f}:  envelope={e:.4f}   d(mu)={m - m**2/4:.4f}")