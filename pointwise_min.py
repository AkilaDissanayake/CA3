import matplotlib.pyplot as plt
import numpy as np

# Define range for x (or mu)
x = np.linspace(-3, 3, 400)

# Create a collection of multiple random/arbitrary linear functions: y = m*x + c
# Representing a family of linear functions L_i(x)
lines = [
    -1.5 * x + 2,
    -0.5 * x - 1,
    0.5 * x + 1,
    1.5 * x - 2,
    -2.0 * x - 3,
    2.0 * x + 3,
]

# Create the plot
plt.figure(figsize=(9, 6))

# Plot each linear function as a thin dashed line
for i, line in enumerate(lines):
    plt.plot(x, line, linestyle="--", alpha=0.6, label=f"Line {i+1}")

# Compute the pointwise minimum (lower envelope) across all lines
lower_envelope = np.minimum.reduce(lines)

# Plot the lower envelope with a bold, distinct line
plt.plot(
    x,
    lower_envelope,
    color="crimson",
    linewidth=3.5,
    label="Pointwise Minimum (Concave Boundary)",
)

# Formatting the plot
plt.xlabel("Variable (e.g., Dual Variable $\mu$)", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.title(
    "Concavity of Pointwise Minimum of Linear Functions", fontsize=14, pad=15
)
plt.xlim(-3, 3)
plt.ylim(-6, 6)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(fontsize=10, loc="lower center", ncol=3)

# Save and show
plt.savefig("concave_lower_envelope_example.png", dpi=300, bbox_inches="tight")
plt.show()