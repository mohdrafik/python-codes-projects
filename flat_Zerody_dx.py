import numpy as np
def flat_zero():
    # Assuming x and y are your data arrays
    # x = your_x_data
    # y = your_y_data
    # Calculate differences between consecutive y-values
    dy = np.diff(y)
    # Define a threshold for detecting flat regions
    slope_threshold = 0.001  # Adjust as needed

    # Find the index where the absolute difference between consecutive y-values is below the threshold
    starting_point_index = np.where(np.abs(dy) < slope_threshold)[0][0]

    # Optionally, refine the starting point by checking neighboring points
    window_size = 5  # Number of neighboring points to consider
    for i in range(starting_point_index, 0, -1):
        if np.all(np.abs(dy[i-window_size:i]) < slope_threshold):
            starting_point_index = i - window_size + 1
        else:
            break

    # Retrieve the corresponding x-value for the starting point
    starting_x_value = x[starting_point_index]

    # Print the starting point
    print("Starting point (x):", starting_x_value)
