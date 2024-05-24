import numpy as np
import matplotlib.pyplot as plt

def logistic_map(x, r):
    return r * x * (1 - x)

def find_period_doubling_bifurcations(r_start, r_end, num_r, iterations, last):
    r_values = np.linspace(r_start, r_end, num_r)
    bifurcation_points = []
    
    for r in r_values:
        x = np.random.rand()
        trajectory = []
        
        for _ in range(iterations):
            x = logistic_map(x, r)
        
        for _ in range(last):
            x = logistic_map(x, r)
            trajectory.append(x)
        
        trajectory = np.array(trajectory)
        unique_points = np.unique(np.round(trajectory, decimals=5))
        
        if len(unique_points) in [2**n for n in range(1, 10)]:
            bifurcation_points.append(r)
    
    return bifurcation_points

def calculate_delta_n(bifurcation_points):
    deltas = []
    for i in range(1, len(bifurcation_points) - 1):
        delta = (bifurcation_points[i] - bifurcation_points[i - 1]) / (bifurcation_points[i + 1] - bifurcation_points[i])
        deltas.append(delta)
    return deltas

# Find bifurcation points
bifurcation_points = find_period_doubling_bifurcations(2.8, 4.0, 10000, 1000, 100)

# Calculate delta_n values
delta_n_values = calculate_delta_n(bifurcation_points)

# Plot the results
n_values = np.arange(1, len(delta_n_values) + 1)

plt.figure(figsize=(10, 6))
plt.plot(n_values, delta_n_values, 'o-', label=r'$\delta_n$', color='blue')
plt.axhline(y=np.sqrt(2), color='red', linestyle='--', label=r'$\delta_n = \sqrt{2}$')

plt.xlabel(r'$n$')
plt.ylabel(r'$\delta_n$')
plt.title(r'Numerical measure of $\delta_n$ for large $n$')
plt.legend()
plt.grid(True)
plt.show()
