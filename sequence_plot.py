import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def bifurcation_diagram_case_i(r0_values, x0, iterations, last):
    for r0 in r0_values:
        r = 2 * r0 - 4
        x = np.zeros(iterations)
        x[0] = x0
        x[1] = x0 + 0.01  # Slightly different initial value to start the iteration
        for i in range(1, iterations - 1):
            if x[i] < x[i - 1]:
                x[i + 1] = 4 * x[i] * (1 - x[i])
            else:
                x[i + 1] = r * x[i] * (1 - x[i])
            # Clamping x[i+1] to be within [0, 1]
            x[i + 1] = min(max(x[i + 1], 0), 1)
        plt.plot([r0] * last, x[-last:], ',k', alpha=0.25)

# Parameters
r0_values = np.linspace(0, 4, 10000)
iterations = 1000
last = 100
x0 = 0.1

# Plot Case (i)
plt.figure(figsize=(10, 6))
bifurcation_diagram_case_i(r0_values, x0, iterations, last)
plt.title('Bifurcation Diagram ')
plt.xlabel('$r_0$')
plt.ylabel('$x_n$')
plt.grid(True)
plt.show()
