import numpy as np
import matplotlib.pyplot as plt

def plot_lagrangian():
    # Define the range of x values
    x = np.linspace(-2.5, 2.5, 400)
    
    # Values of mu to plot
    mu_values = [0, 1, 2, 3]
    
    # Setup the plot
    plt.figure(figsize=(10, 6))
    colors = ['blue', 'orange', 'green', 'red']
    
    for mu, color in zip(mu_values, colors):
        # Calculate Lagrangian L(mu, x)
        L = x**2 + mu * (1 - x)
        
        # Calculate the minimizer x(mu) = mu / 2
        x_min = mu / 2
        L_min = x_min**2 + mu * (1 - x_min)
        
        # Plot the curve
        plt.plot(x, L, label=f'$\mu={mu}$', color=color)
        
        # Mark the minimizer
        plt.plot(x_min, L_min, marker='o', markersize=8, color=color, 
                 markeredgecolor='black', zorder=5)
        
        # Add a text annotation for the minimizer
        plt.annotate(f'  $x^*({mu})={x_min}$', (x_min, L_min), 
                     textcoords="offset points", xytext=(0,10), ha='center')

    # Formatting the plot
    plt.axvline(x=1, color='gray', linestyle='--', label='Constraint $x \geq 1$')
    plt.title('Lagrangian $L(\mu, x) = x^2 + \mu(1-x)$ for given $\mu$')
    plt.xlabel('$x$')
    plt.ylabel('$L(\mu, x)$')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.legend()
    plt.ylim(-1, 5)

    plt.savefig('lagrangian_plot.png', dpi=300, bbox_inches='tight')
    # Show the plot
    plt.show()

# Execute the function
if __name__ == "__main__":
    plot_lagrangian()