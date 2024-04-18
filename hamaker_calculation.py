import pandas as pd
import numpy as np
import os
from termcolor import colored

def hamaker_save_data(data_path, ampfrominflexion2flat_nm, phasefrominflexion2flat_degree, piezofrominflexion2flat_nm, filenameAmplitude, filenamephase, A0, K = 2.56, Q = 234, R = 10e-9):
    
    ampfrominflexion2flat_nm = ampfrominflexion2flat_nm.reset_index(drop=True)
    phasefrominflexion2flat_degree = phasefrominflexion2flat_degree.reset_index(drop=True)
    piezofrominflexion2flat_nm  = piezofrominflexion2flat_nm.reset_index(drop=True)
    
    # Convert values to meters and radians
    amp_df_meter = ampfrominflexion2flat_nm / 1e9
    piezo_df_meter = piezofrominflexion2flat_nm / 1e9
    phase_df_radian = np.radians(phasefrominflexion2flat_degree)

    # Calculate Hamaker values
    hamaker_values = ((-3 * K * A0) / (Q * R)) * ((amp_df_meter ** 2) * np.cos(phase_df_radian)) * ((((piezo_df_meter + amp_df_meter) / amp_df_meter) ** 2) - 1) ** 1.5

    # Create DataFrame with columns 'piezo', 'amplitude', 'phase', and 'hamaker_values'
    df = pd.DataFrame({
        'piezo_meter': piezo_df_meter,
        'amplitude_meter': amp_df_meter,
        'phase_degree': phasefrominflexion2flat_degree,
        'phase_rad': phase_df_radian,
        'hamaker_values': hamaker_values
    })

    # Create directory 'hamaker_data' if it doesn't exist
    hamaker_dir = os.path.join(data_path, 'hamaker_data')
    if not os.path.exists(hamaker_dir):
        os.makedirs(hamaker_dir)

    # Save DataFrame to Excel file in 'hamaker_data' directory
    # hamaker_filename = filenameAmplitude[0:-5]+filenamephase[0:-5]+'hamaker.xlsx'
    
    hamaker_filename = filenameAmplitude[:-5] + filenamephase[:-5]+"hamaker.xlsx"
    excel_file_path = os.path.join(hamaker_dir, hamaker_filename)
    df.to_excel(excel_file_path, index=False)
