import numpy as np
import matplotlib.pyplot as plt 

# Data points
x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def divided_diff_table(x_points, y_points):
    n = len(x_points)
    table = np.zeros((n, n))
    table[:,0] = y_points
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x_points[i+j] - x_points[i])
    
    return table

def newton_interpolation(x_points, y_points, x):
    table = divided_diff_table(x_points, y_points)
    n = len(x_points)
    result = table[0, 0]
    product_term = 1.0
    
    for i in range(1, n):
        product_term *= (x - x_points[i-1])
        result += table[0, i] * product_term
    
    return result

# Generate interpolated values
x_values = np.linspace(5, 40, 100)
y_values_newton = [newton_interpolation(x_points, y_points, x) for x in x_values]

# Plotting
plt.plot(x_points, y_points, 'o', label='Data Points')
plt.plot(x_values, y_values_newton, label='Newton Interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()
