import matplotlib.pyplot as plt
import numpy as np

# Define range for the dual variable mu
mu = np.linspace(0, 4, 400)

# Lagrangian lines for x = 0, 1, 2
L0 = mu  # L(mu, 0) = 0^2 + mu(1 - 0) = mu
L1 = np.ones_like(mu) * 1  # L(mu, 1) = 1^2 + mu(1 - 1) = 1
L2 = 4 - mu  # L(mu, 2) = 2^2 + mu(1 - 2) = 4 - mu

# Lower envelope of the three lines (pointwise minimum)
lower_envelope = np.minimum(np.minimum(L0, L1), L2)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(
    mu, L0, label=r"$L(\mu, 0) = \mu$", linestyle="--", color="royalblue"
)
plt.plot(
    mu, L1, label=r"$L(\mu, 1) = 1$", linestyle="--", color="forestgreen"
)
plt.plot(
    mu, L2, label=r"$L(\mu, 2) = 4 - \mu$", linestyle="--", color="darkorange"
)
plt.plot(
    mu,
    lower_envelope,
    label=r"Lower Envelope",
    linewidth=3,
    color="crimson",
)

# Formatting the plot
plt.xlabel(r"Dual Variable $\mu$", fontsize=12)
plt.ylabel(r"Lagrangian $L(\mu, x)$", fontsize=12)
plt.title(
    "Lagrangian Lines and Lower Envelope",
    fontsize=14,
    pad=15,
)
plt.xlim(0, 4)
plt.ylim(0, 5)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(fontsize=11, loc="upper right")

plt.savefig("lagrangian_lower_envelope.png", dpi=300, bbox_inches="tight")
# Show the plot
plt.tight_layout()
plt.show()