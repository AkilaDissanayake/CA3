import numpy as np
import matplotlib.pyplot as plt

def plot_saddle_point():
    # Define ranges for mu and x
    mu = np.linspace(0, 4, 300)
    x = np.linspace(-1, 3, 300)
    
    # Calculate function values
    L_mu_xstar = np.ones_like(mu)          # L(mu, x*) = 1 for all mu
    L_mustar_x = (x - 1)**2 + 1             # L(mu*, x) = (x - 1)^2 + 1
    
    # Optimal points
    mu_star = 2
    x_star = 1
    L_star = 1

    # Create two side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # --- Plot 1: L(mu, x*) vs mu ---
    ax1.plot(mu, L_mu_xstar, color='crimson', linewidth=2.5, label='$L(\\mu, x^*) = 1$')
    ax1.scatter([mu_star], [L_star], color='gold', edgecolor='black', s=120, zorder=5, 
                label='Saddle Point $(\\mu^*, L^*) = (2, 1)$')
    
    ax1.set_title('$L(\\mu, x^*)$ vs $\\mu$ (Fixed $x^* = 1$)', fontsize=12, pad=10)
    ax1.set_xlabel('$\\mu$', fontsize=11)
    ax1.set_ylabel('$L(\\mu, x^*)$', fontsize=11)
    ax1.set_xlim(-0.2, 4)
    ax1.set_ylim(0, 3)
    ax1.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax1.legend(loc='upper right')
    
    # Annotate point
    ax1.annotate('$L(\\mu^*, x^*) = 1$', (mu_star, L_star), textcoords="offset points", 
                 xytext=(0, 12), ha='center', fontweight='bold')

    # --- Plot 2: L(mu*, x) vs x ---
    ax2.plot(x, L_mustar_x, color='royalblue', linewidth=2.5, label='$L(\\mu^*, x) = (x-1)^2 + 1$')
    ax2.scatter([x_star], [L_star], color='gold', edgecolor='black', s=120, zorder=5, 
                label='Saddle Point $(x^*, L^*) = (1, 1)$')
    
    ax2.set_title('$L(\\mu^*, x)$ vs $x$ (Fixed $\\mu^* = 2$)', fontsize=12, pad=10)
    ax2.set_xlabel('$x$', fontsize=11)
    ax2.set_ylabel('$L(\\mu^*, x)$', fontsize=11)
    ax2.set_xlim(-1, 3)
    ax2.set_ylim(0, 6)
    ax2.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax2.legend(loc='upper right')
    
    # Annotate point
    ax2.annotate('$L(\\mu^*, x^*) = 1$', (x_star, L_star), textcoords="offset points", 
                 xytext=(0, 12), ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('saddle_point_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    plot_saddle_point()