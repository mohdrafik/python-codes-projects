import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import chisquare

# Define the potential functions
def repulsive_inverse_power(r, A, alpha):
    return A / r**alpha

def attractive_exponential(r, B, C):
    return -B * np.exp(-C * r)

def attractive_inverse_power(r, D, beta):
    return -D / r**beta

def combined_function_exponential(r, A, alpha, B, C):
    return repulsive_inverse_power(r, A, alpha) + attractive_exponential(r, B, C)

def combined_function_inverse_power(r, A, alpha, D, beta):
    return repulsive_inverse_power(r, A, alpha) + attractive_inverse_power(r, D, beta)

# Function to fit data and calculate chi-square
def fit_data_and_calculate_chi_square(r, V, fit_function, p0, bounds):
    popt, pcov = curve_fit(fit_function, r, V, p0=p0, bounds=bounds)
    V_fit = fit_function(r, *popt)
    chi2, p = chisquare(f_obs=V, f_exp=V_fit)
    return popt, chi2, V_fit

# Main function to perform the fitting and save the results
def best_fit_function(r, V):
    # Initial guesses and bounds for the parameters
    initial_guesses_exp = [1.0, 12, 1.0, 1.0] # [A, alpha, B, C]
    bounds_exp = (0, np.inf)
    
    initial_guesses_inv = [1.0, 12, 1.0, 6] # [A, alpha, D, beta]
    bounds_inv = (0, np.inf)
    
    # Fit with exponential attractive part
    popt_exp, chi2_exp, V_fit_exp = fit_data_and_calculate_chi_square(r, V, combined_function_exponential, initial_guesses_exp, bounds_exp)
    
    # Fit with inverse power attractive part
    popt_inv, chi2_inv, V_fit_inv = fit_data_and_calculate_chi_square(r, V, combined_function_inverse_power, initial_guesses_inv, bounds_inv)
    
    # Choose the best fit
    if chi2_exp < chi2_inv:
        best_fit = 'Exponential'
        best_popt = popt_exp
        best_V_fit = V_fit_exp
        best_chi2 = chi2_exp
    else:
        best_fit = 'Inverse Power'
        best_popt = popt_inv
        best_V_fit = V_fit_inv
        best_chi2 = chi2_inv
    
    # Save the results in a DataFrame
    results = pd.DataFrame({'r': r, 'V': V, 'V_fit': best_V_fit})
    
    return best_fit, best_popt, best_chi2, results

# Example usage
if __name__ == "__main__":
    # Example data (replace with actual data)
    r = np.linspace(1, 10, 100)
    V = repulsive_inverse_power(r, 10, 12) + attractive_exponential(r, 5, 6) + np.random.normal(0, 0.5, r.size)
    print(V)
    best_fit, best_popt, best_chi2, results = best_fit_function(r, V)
    
    print(f"Best fit function: {best_fit}")
    print(f"Optimized parameters: {best_popt}")
    print(f"Chi-square value: {best_chi2}")
    print(results.head())

    # Save the DataFrame to a CSV file
    results.to_csv('fitting_results.csv', index=False)
