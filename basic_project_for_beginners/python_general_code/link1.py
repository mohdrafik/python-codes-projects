# x =range(0,1)
# for i in range(0,1):
#     print(i)
#     for j in range(0,1):
#         print(j)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Sample data (replace this with your actual data)
x = np.linspace(0, 10, 100)
y = 2 * np.sin(x) + np.random.normal(0, 0.1, 100)

# Plot the original data
plt.plot(x, y, label='Original Data')

# Find peaks (minima) in the data
minima_indices, _ = find_peaks(-y)

# Plot detected minima
plt.plot(x[minima_indices], y[minima_indices], 'rx', label='Detected Minima')

# Identify regions with approximately constant values
constant_regions = []
current_region = [minima_indices[0]]
for i in range(1, len(minima_indices)):
    if x[minima_indices[i]] - x[minima_indices[i - 1]] > threshold:
        constant_regions.append(current_region)
        current_region = [minima_indices[i]]
    else:
        current_region.append(minima_indices[i])

# Add the last region
constant_regions.append(current_region)

# Highlight constant regions
for region in constant_regions:
    plt.axvspan(x[region[0]], x[region[-1]], facecolor='gray', alpha=0.2)

plt.legend()
plt.show()
