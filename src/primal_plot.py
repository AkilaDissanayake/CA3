import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

PLOTS_DIR = Path(__file__).resolve().parent.parent / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

def plot_primal():
    # Setup the plot
    plt.figure(figsize=(10, 6))
    
    # Define x ranges
    x_feasible = np.linspace(1, 3, 200)
    x_all = np.linspace(-1, 3, 400)
    
    # Plot the original objective function x^2 for reference
    plt.plot(x_all, x_all**2, 'k--', alpha=0.4, label='Original Objective $f(x) = x^2$')
    
    # Plot the primal function in the feasible region
    plt.plot(x_feasible, x_feasible**2, 'b-', linewidth=3, 
             label='$g(x) = x^2$ (Feasible Region)')
    
    # Shade the infeasible region
    plt.axvspan(-1, 1, color='red', alpha=0.15)

    # Insert text labels directly inside the regions
    plt.text(0.0, 5.0, 'Infeasible Region\n$g(x) = +\infty$\n($x < 1$)', 
             color='red', fontsize=12, fontweight='bold', ha='center', va='center')
    
    plt.text(2.5, 2.0, 'Feasible Region\n$g(x) = x^2$\n($x \geq 1$)', 
             color='blue', fontsize=12, fontweight='bold', ha='center', va='center')

    # Formatting the plot
    plt.title('Primal Function $g(x) = \max_{\mu \geq 0} L(\mu, x)$')
    plt.xlabel('$x$')
    plt.ylabel('$g(x)$')
    plt.xlim(-1, 3)
    plt.ylim(0, 10)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.legend(loc='upper left')
    
    # Save and show
    plt.savefig(PLOTS_DIR / "primal_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot_primal()