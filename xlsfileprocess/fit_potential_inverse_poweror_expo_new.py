import numpy as np
import matplotlib.pyplot as plt

def potential_function(r, A, n, B, C):
    """
    Combined potential function:
    V(r) = A / r^n - B * exp(-C*r)
    """
    return A / r**n - B * np.exp(-C*r)

# Generate example data
distance = np.linspace(0.5, 10, 1000)
potential = potential_function(distance, 1e-49, 12, 1e-18, 1e9)

# Find the minimum point (equilibrium distance)
equilibrium_index = np.argmin(potential)
equilibrium_distance = distance[equilibrium_index]

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(distance, potential, 'b-', linewidth=2)

# Mark repulsive region
plt.fill_between(distance[:equilibrium_index], potential[:equilibrium_index], 
                 where=(distance[:equilibrium_index] < equilibrium_distance),
                 color='red', alpha=0.3, label='Repulsive Region')

# Mark attractive region
plt.fill_between(distance[equilibrium_index:], potential[equilibrium_index:], 
                 where=(distance[equilibrium_index:] > equilibrium_distance),
                 color='green', alpha=0.3, label='Attractive Region')

# Add labels and title
plt.xlabel('Distance (nm)', fontsize=14)
plt.ylabel('Potential Energy (1e-18 J)', fontsize=14)
plt.title('Interatomic Potential Energy Curve', fontsize=16)

# Add legend
plt.legend(fontsize=12)

# Set y-axis limits to focus on the well
plt.ylim(-1.5e-18, 1e-18)

# Add text annotations
plt.annotate('Equilibrium Distance', xy=(equilibrium_distance, potential[equilibrium_index]),
             xytext=(equilibrium_distance+1, potential[equilibrium_index]-0.5e-18),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# import numpy as np
# import pandas as pd
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt

# def potential_function(r, A, n, B, C):
#     """
#     Combined potential function:
#     V(r) = A / r^n - B * exp(-C*r)
#     """
#     return A / r**n - B * np.exp(-C*r)

# def fit_potential(distance, potential):
#     """
#     Fit the potential curve and calculate chi-square.
#     """
#     # Initial guess for parameters
#     p0 = [1e-50, 12, 1e-18, 1e9]
    
#     # Fit the curve
#     popt, pcov = curve_fit(potential_function, distance, potential, p0=p0)
    
#     # Generate fitted values
#     potential_fit = potential_function(distance, *popt)
    
#     # Calculate chi-square
#     chi_square = np.sum((potential - potential_fit)**2 / np.abs(potential_fit))
    
#     # Degrees of freedom
#     dof = len(potential) - len(popt)
    
#     # Create DataFrame
#     df = pd.DataFrame({
#         'Distance (nm)': distance,
#         'Measured Potential (1e-18 J)': potential,
#         'Fitted Potential (1e-18 J)': potential_fit
#     })
    
#     return popt, chi_square, dof, df

# # Example usage (you'll need to replace this with your actual data)
# # Generate some sample data
# distance = np.linspace(0.1, 6, 100)
# true_potential = potential_function(distance, 1e-50, 12, 1e-18, 1e9)
# noise = np.random.normal(0, 1e-19, distance.shape)
# measured_potential = true_potential + noise

# # Fit the curve
# params, chi_square, dof, results_df = fit_potential(distance, measured_potential)

# # Print results
# print(f"Fitted parameters: A={params[0]:.2e}, n={params[1]:.2f}, B={params[2]:.2e}, C={params[3]:.2e}")
# print(f"Chi-square: {chi_square:.4f}")
# print(f"Degrees of freedom: {dof}")

# # Plot the results
# plt.figure(figsize=(10, 6))
# plt.scatter(distance, measured_potential, label='Measured Data', alpha=0.5)
# plt.plot(distance, results_df['Fitted Potential (1e-18 J)'], 'r-', label='Fitted Curve')
# plt.xlabel('Distance (nm)')
# plt.ylabel('Potential (1e-18 J)')
# plt.legend()
# plt.title('Potential Energy Curve Fitting')
# plt.show()

# # Save results to CSV
# results_df.to_csv('potential_fit_results.csv', index=False)