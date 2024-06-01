import numpy as np
import matplotlib.pyplot as plt
from langrange import langrange_interpolation

# Data points
x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])


# Test points for interpolation
test_x_values = [7.5, 12.5, 22.5, 27.5, 37.5]

# Test Langrange interpolation
print("Langrange Interpolation Results:")
for x in test_x_values:
    y = langrange_interpolation(x_points, y_points, x)
    print(f"Interpolated value at x = {x}: y = {y}")