import numpy as np
import matplotlib.pyplot as plt

def delta_n(r_values):
    deltas = []
    for i in range(1, len(r_values) - 1):
        delta = (r_values[i] - r_values[i - 1]) / (r_values[i + 1] - r_values[i])
        deltas.append(delta)
    return deltas

def find_r_values(num_r0=1000, epsilon=1e-3):
    r_values = []
    r0 = 2.0
    while r0 < 4.0:
        x = np.random.rand()
        for _ in range(1000):
            x = (r0 - (4 - r0) * np.tanh((x - 0.5) / epsilon)) * x * (1 - x)
        r_values.append(r0)
        r0 += (4.0 - 2.0) / num_r0
    return r_values

# Generate r values
r_values = find_r_values()

# Calculate delta_n values
deltas = delta_n(r_values)

# Plot the results
plt.figure(figsize=(10, 6))
n_values = np.arange(1, len(deltas) + 1)

plt.plot(n_values, deltas, label=r'$\delta_n$', color='blue', marker='o', linestyle='-')
plt.axhline(y=np.sqrt(2), color='red', linestyle='--', label=r'$\delta_n = \sqrt{2}$')

plt.xlabel(r'$n$')
plt.ylabel(r'$\delta_n$')
plt.title(r'Numerical measure of $\delta_n$ for large $n$')
plt.legend()
plt.grid(True)
plt.show()
