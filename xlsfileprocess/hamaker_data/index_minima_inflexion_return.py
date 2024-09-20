

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.io as sio
import os
from termcolor import colored
import logging  
import sys
sys.path.append('E:\\python_programs\\xlsfileprocess\\')
# from listxlsfilesinOrder import listxlsFiles
# from converdfSetAxisgetNumpyArray import readASdfsetaxisAmpasnp
from plotmatlabfun import plot_data
from reverseArrayOfAvgWindow import reverseArrayofAvgValuesWndsize
from detect_inflexiondy_dxZero import detect_inflexion_pointAfterAverage
from final_index_calculation import findActualInflexion
import average_windowsize as avgws
import inflexionMinimadownbump as smfitbp 
import fitselectdataRange1bymfind as fitsmoothsave
# from savefiledf2dat import filesaveDatain_dat
# from potential_force import potential_force_algo
# from hamaker_calculation import hamaker_save_data



def find_indexOfminima_inflexion(df, file_No):

    point_density_OLd = 8910.417881801475  # corresponds to avg_windowsize = 4.
    avg_windowsize = 4 

    print(f"I have read and converted the data in dataframe and numpy array and no of row in amp as data_endamp for file {i+1} named as {filenameAmplitude} and {filenamephase}.")
    # res = readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase)

    
    ampdf = res[0]        # ampdf is two column dataframe with title: ['Piezo','Amplitude'] piezo(um) and Amplitude(nA) 
    phasedf = res[1]      # phasedf is two column dataframe with title: ['Piezo','Phase']
    data_endamp = res[2]   #  total length of ampdf, index of the last value is --> data_endamp-1
    ampdfPiezoColumnarr = res[3]  # it is single column Piezo numpy array  only
    ampdfAmplitudeColumnarr = res[4]    # it is single column  amplitude numpy array only
    A0 = res[5]    # A0 is the last value of the ampdf Amplitude  ***********  check for A0 values if this is in m . I think it is in nA here.

    plt.figure()
    plot_data(ampdf,label='amp',color='blue', marker='', markersize=1,alpha=0.8,title=f"amplitude Vs Piezo {i+1}/{sameNo_of_amp_phase_length}th_data, out of {sameNo_of_amp_phase_length}",Xaxis="Piezo",Yaxis='Amplitude')
    plt.show()
    plt.figure()
    plot_data(phasedf,label='phase',color='red', marker='', markersize=1,alpha=0.6,title=f"Phase Vs Piezo {i+1}/{sameNo_of_amp_phase_length}th_data, out of {sameNo_of_amp_phase_length}",Xaxis="Piezo",Yaxis='Phase')
    plt.show()

    # ------------ *********** here add a function to calculate the avg_window size for each file individually.

    avg_windowsize1 = avgws.calculate_avg_wndsize_Individual_filewise(ampdfPiezoColumnarr,file_No,point_density_OLd,avg_windowsize)
    avg_window = avg_windowsize1  # 7,4(more general)  # ******************

    list_avg = reverseArrayofAvgValuesWndsize(ampdf,phasedf,avg_window)  # list_avg -> reversed numpy array.
    #     plt.figure()
    #     plot_data(list_avg,label=f"avg of {avg_window} ",title=f"avg plot of reverse {avg_window} data points for {i+1} file")
    #     plt.show()

    consecutive_decrease_windowsize = 3   #6,6(3,6 more general)
    index = detect_inflexion_pointAfterAverage(ampdf,list_avg,consecutive_decrease_windowsize) 
    inflexion_After_avg =  index
    print("index of inflexion point w.r.to the average list(i.e. in list_avg) :",inflexion_After_avg,"<-->")
    final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr,want_plot=1)
    #     final_Actual_index = findActualInflexion(inflexion_After_avg,list_avg,data_endamp,avg_window,ampdfAmplitudeColumnarr,ampdfPiezoColumnarr)
    zero_orFlatAmp = final_Actual_index    #  this the actual index from where we get flat amplitude almost,,after bump Flat region start.
    print(zero_orFlatAmp )
    print(ampdf.iloc[final_Actual_index,0])

    # <--------- it is for the finding the downbump in the actual data ... >
    res_indices = smfitbp.findDownBump(ampdf, zero_orFlatAmp, window_length=30, polyorder=3)
    index_inflexion = res_indices[0]
    print("\n index_inflexion ---------->",index_inflexion)
    index_minima = res_indices[1]
    print("\n index_minima ---------->",index_minima)
    smoothed_array = res_indices[4]  # it returned the smoothed array after filtering.