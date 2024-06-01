import numpy as np
import matplotlib.pyplot as plt

def langrange_interpolation(x_points, y_points, x):
    def langrange_basis(j):
        basis = [(x - x_points[m]) / (x_points[j] - x_points[m]) for m in range(len(x_points)) if m != j]
        return np.prod(basis, axis=0)
    
    return sum(y_points[j] * langrange_basis(j) for j in range(len(x_points)))

# Data points
x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Generate interpolated values
x_values = np.linspace(5, 40, 100)
y_values_langrange = [langrange_interpolation(x_points, y_points, x) for x in x_values]

# Plotting
plt.plot(x_points, y_points, 'o', label='Data Points')
plt.plot(x_values, y_values_langrange, label='Langrange Interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Langrange')
plt.legend()
plt.grid(True)
plt.show()
