import numpy as np
import matplotlib.pyplot as plt

def plot_primal():
    # Setup the plot
    plt.figure(figsize=(10, 6))
    
    # Define x ranges
    x_infeasible = np.linspace(-1, 1, 200)
    x_feasible = np.linspace(1, 3, 200)
    x_all = np.linspace(-1, 3, 400)
    
    # Plot the original objective function x^2 for reference
    plt.plot(x_all, x_all**2, 'k--', alpha=0.4, label='Original Objective $f(x) = x^2$')
    
    # Plot the primal function in the feasible region
    plt.plot(x_feasible, x_feasible**2, 'b-', linewidth=3, 
             label='$g(x) = x^2$ (Feasible Region)')
    
    # Indicate the infinite penalty in the infeasible region
    plt.axvspan(-1, 1, color='red', alpha=0.15, label='Infeasible Region $x < 1 \implies g(x) = +\infty$')
    plt.axvline(x=1, color='red', linestyle='-', linewidth=2)
    
    # Add an upward arrow and text to symbolize +infinity at the boundary
    plt.annotate('', xy=(0.5, 9), xytext=(0.5, 3),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=8, alpha=0.5))
    plt.text(0.5, 6, '$g(x) = +\infty$', color='red', fontsize=14, 
             ha='center', va='center', rotation=90, alpha=0.7)

    # Formatting the plot
    plt.title('Primal Function $g(x) = \max_{\mu \ge 0} L(\mu, x)$')
    plt.xlabel('$x$')
    plt.ylabel('$g(x)$')
    plt.xlim(-1, 3)
    plt.ylim(0, 10)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.legend(loc='upper left')
    
    # Save and show
    plt.savefig('primal_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot_primal()