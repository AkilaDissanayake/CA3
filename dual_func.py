import numpy as np
import matplotlib.pyplot as plt

def plot_dual():
    # Define the range of mu values (mu >= 0)
    mu = np.linspace(0, 4.5, 400)
    
    # Calculate the dual function d(mu) = mu - mu^2 / 4
    d_mu = mu - (mu**2) / 4
    
    # Dual optimal values
    mu_star = 2
    d_star = 1
    
    # Setup the plot
    plt.figure(figsize=(10, 6))
    
    # Plot d(mu)
    plt.plot(mu, d_mu, label='$d(\mu) = \mu - \\frac{\mu^2}{4}$', color='purple', linewidth=2)
    
    # Mark the maximum (mu*, d*)
    plt.plot(mu_star, d_star, marker='*', markersize=12, color='black', 
             markeredgecolor='black', zorder=5, label='Optimal Dual $(\mu^*, d^*)$')
    
    # Annotate the maximum
    plt.annotate(f'  $(\mu^*={mu_star}, d^*={d_star})$', (mu_star, d_star), 
                 textcoords="offset points", xytext=(0,10), ha='center')
                 
    # Formatting the plot
    plt.title('Dual Function $d(\mu)$ vs $\mu$')
    plt.xlabel('$\mu$ (Dual Variable)')
    plt.ylabel('$d(\mu)$ (Dual Value)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Highlight the feasible region for mu (mu >= 0)
    plt.axvspan(-0.5, 0, color='gray', alpha=0.2, label='Infeasible $\mu < 0$')
    
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.legend()
    plt.xlim(-0.5, 4.5)
    plt.ylim(-0.5, 1.5)
    
    # Save and show
    plt.savefig('dual_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot_dual()