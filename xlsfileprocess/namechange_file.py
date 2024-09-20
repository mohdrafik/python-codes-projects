import os
path = "E:\\python_programs\\xlsfileprocess\\pdata\\"
for file in os.listdir(path):
    print(file)
    if file.endswith('.spec'):
        # print(file)
        print(file)
        new_filename = file[0:-5]
        print(new_filename)
        # or file in os.listdir(path):
    # if '.spec' in file:
        # new_filename = file.replace('.spec', '')
        os.rename(os.path.join(path, file), os.path.join(path,new_filename))
        import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
from scipy.stats import zscore
import os
    # Load the data
    data = pd.read_csv(filename, delim_whitespace=True, header=None, names=['distance', 'potential', 'dissipation', 'Kvalue'])

    distance = data['distance'].values
    potential = data['potential'].values

    # Step 2: Remove outliers using z-score
    z_scores = zscore(potential)
    threshold = 3  # Define the threshold for outliers
    filtered_indices = np.abs(z_scores) < threshold

    distance_filtered = distance[filtered_indices]
    potential_filtered = potential[filtered_indices]

    # Step 3: Remove duplicate distance values
    unique_indices = np.unique(distance_filtered, return_index=True)[1]
    distance_filtered = distance_filtered[unique_indices]
    potential_filtered = potential_filtered[unique_indices]

    # Step 4: Plotting Potential vs. Distance (Filtered)
    plt.figure(figsize=(10, 6))
    plt.scatter(distance_filtered, potential_filtered, label='Filtered Data', color='blue')
    plt.xlabel('Distance')
    plt.ylabel('Potential')
    plt.title('Filtered Potential vs. Distance')
    plt.legend()
    plt.show()

    # Step 5: Fitting a Polynomial to Filtered Data
    def polynomial(x, *coeffs):
        return np.polyval(coeffs, x)

    degree = 3  # Change the degree as needed
    popt, _ = curve_fit(lambda x, *params: polynomial(x, *params), distance_filtered, potential_filtered, p0=[1]*degree)
    fitted_potential = polynomial(distance_filtered, *popt)

    plt.figure(figsize=(10, 6))
    plt.scatter(distance_filtered, potential_filtered, label='Filtered Data', color='blue')
    plt.plot(distance_filtered, fitted_potential, label=f'Fitted Polynomial (degree {degree})', color='red')
    plt.xlabel('Distance')
    plt.ylabel('Potential')
    plt.title('Polynomial Fit of Filtered Potential vs. Distance')
    plt.legend()
    plt.show()

    # Step 6: Calculating the Force (Negative Gradient of the Potential)
    # Smoothing the potential data
    smoothed_potential = savgol_filter(fitted_potential, 51, 3)  # window size 51, polynomial order 3

    # Ensure the distance values are unique and well-spaced
    diff_distance = np.diff(distance_filtered)
    distance_filtered = distance_filtered[np.insert(diff_distance > 1e-12, 0, True)]

    # Calculate force by differentiating the smoothed potential
    force = -np.gradient(smoothed_potential, distance_filtered)

    # Step 7: Plotting and Saving the Results
    # Plot and save smoothed potential data
    plt.figure(figsize=(10, 6))
    plt.plot(distance_filtered, smoothed_potential, label='Smoothed Potential', color='green')
    plt.xlabel('Distance')
    plt.ylabel('Potential')
    plt.title('Smoothed Potential vs. Distance')
    plt.legend()
    plt.savefig('smoothed_potential.png')
    plt.show()

    # Plot and save force data
    plt.figure(figsize=(10, 6))
    plt.plot(distance_filtered, force, label='Force', color='purple')
    plt.xlabel('Distance')
    plt.ylabel('Force')
    plt.title('Force vs. Distance')
    plt.legend()
    plt.savefig('force.png')
    plt.show()



    

