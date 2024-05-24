import numpy as np
import matplotlib.pyplot as plt

def logistic_map_memory_coupled(r0, x, xc, epsilon):
    return (r0 - (4 - r0) * np.tanh((x - xc) / epsilon)) * x * (1 - x)

def bifurcation_diagram(xc, epsilon, r0_start=2.0, r0_end=4.0, num_r0=5000, num_iter=5000, last=100):
    r0_values = np.linspace(r0_start, r0_end, num_r0)
    x_values = np.zeros(num_r0)
    for i, r0 in enumerate(r0_values):
        x = np.random.rand()
        for _ in range(num_iter):
            x = logistic_map_memory_coupled(r0, x, xc, epsilon)
        x_values[i] = x
    
    plt.figure(figsize=(10, 6))
    plt.plot(np.log(r0_values - 2), np.log(x_values), 'ok', alpha=0.25, markersize=2)
    plt.xlabel(r'$\log(r_0 - 2)$')
    plt.ylabel(r'$\log(x_n)$')
    plt.title(f'Bifurcation diagram with $x_c = {xc}$')
    plt.grid(True)
    plt.show()

epsilon = 1e-3  # Assuming epsilon -> 0
cutoffs = [0.5]

for xc in cutoffs:
    bifurcation_diagram(xc, epsilon)
