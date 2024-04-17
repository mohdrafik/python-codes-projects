# backward_MinimaBump_nmValue = 4.0
# forward_MinimaBump_nmValue = 10.0

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

def find1bymcampdfandfit(ampdf,phasedf,backward_MinimaBump_nmValue,forward_MinimaBump_nmValue,res_indices,data_endamp,i,zero_orFlatAmp,part2 =None):

    xpiezo_nm = 1000*ampdf['Piezo']  # now xpiezo_nm in nm --> after multiplying by 1000 become in nm 
    x_diff = np.diff(ampdf['Piezo'])
    d_nm = 1000*x_diff[5]   # this is in nanometer (nm) now. 
    dataselect1 = zero_orFlatAmp
    # print("d in nm \t:",d_nm)
    # count = 0
    # for val in x_diff:
    #     # just to check common differences between piezo values.
    #     count = count+1
    #     print(val)
    #     if count ==5:
    #         break
            
    # plt.plot(list(range(len(x_diff))), ampdf['Piezo'])    
    # plt.show()
    # #     print()

    # here 2.5,3nm any value we put get corresponding N 
    # backward_MinimaBump_nmValue = 4.0  # <------------- make it as argument in func.
    N_count_back = (backward_MinimaBump_nmValue)/(d_nm)  # (using a+(n-1)D)

    N_count_back = np.ceil(N_count_back)
    print("n count back = ",N_count_back)

    desired_nmBackIndexwrtoInflexion = res_indices[0] - N_count_back  # it is from the inflexion point
    desired_nmBackIndexwrtoMinima = res_indices[1] - N_count_back  # this is from the minima point
    # desired_nmBackIndex
    # now time to choose the data 3nm after the minima(bump):
    # forward_MinimaBump_nmValue = 10.0     # <------------- make it as argument in func.
    
    N_count_forward = (forward_MinimaBump_nmValue)/(d_nm)  # (using a+(n-1)D)
    N_count_forward = np.ceil(N_count_forward)
    data_choose_endindex = res_indices[1] + int(N_count_forward)
    data_choose_endindex = data_endamp

    print("\n index starting wrto inflexion : ",desired_nmBackIndexwrtoInflexion, 
        "\n index starting wrto Minima : ",desired_nmBackIndexwrtoMinima)

    desired_nmBackIndexwrtoInflexion = int(desired_nmBackIndexwrtoInflexion)
    desired_nmBackIndexwrtoMinima = int(desired_nmBackIndexwrtoMinima)



    ##### ----------this is for linear fitting the data from desired point to the inflexion points data :-----------##
    # Perform linear regression for linear fitting
    index_inflexion = res_indices[0]   # < -- it is inflexion point 
    ampdf_x_nm = 1000*ampdf['Piezo'][desired_nmBackIndexwrtoInflexion:index_inflexion]
    ampdf_y_nA = ampdf['Amplitude'][desired_nmBackIndexwrtoInflexion:index_inflexion]

    coefficients = np.polyfit(ampdf_x_nm,ampdf_y_nA, 1)

    m, c = coefficients
    # Print the results
    print(f"m (slope in nA/nm ): for {i+1} file data {m}")
    print(f"c, zero intercept nA (intercept): for {i+1} file data {c}")

    ampdf_y_nm = (1/m)*ampdf_y_nA    #--------****** save this data as Amplitude in .dat file----------*********** 

    poly = np.poly1d(coefficients)  # this is like f(x) = m*x + c , give x values get y values.

    # Plot the data and the linear fit
    fig, ax1 = plt.subplots()
    ax1.plot(ampdf_x_nm,ampdf_y_nm, marker ='.',label='Data(nm)')
    ax1.set_xlabel('piezo(nm)')
    ax1.set_ylabel('Amplitude(nm)',color='b')
    ax1.tick_params('y', colors='b')  # this will make blue color font on y axis left side.
    ax1.grid()
    ax1.legend()

    ax2= ax1.twinx()  # it will share the x axis --> twinx()
    ax2.plot(ampdf_x_nm, ampdf_y_nA, color='green',marker ='.',label='Data(nA)')
    ax2.plot(ampdf_x_nm, poly(ampdf_x_nm), color='red', label='Linear Fit') 
    ax2.set_xlabel('piezo(nm)')
    ax2.set_ylabel('Amplitude(nA)',color='r')
    ax2.tick_params('y',colors = 'r')
    ax2.set_ylim([6,10])
    # ax2.set_grid()
    ax2.legend(loc=[0.02,0.79])
    plt.title('Linear fitting of the ampltitude and piezo data')
    plt.show()


    # ************ ------------ this is working fine for me ----------------------******************
    # same data but another figure 

    fig
    plt.scatter(ampdf_x_nm, ampdf_y_nA, marker ='.',label='Data(nA)')

    plt.scatter(ampdf_x_nm,ampdf_y_nm, marker ='*',label='Data(nm)') # THIS IS FOR CONVERTED Y DATA TO nm --> y=  y*(1/m)

    plt.plot(ampdf_x_nm, poly(ampdf_x_nm), color='red', label='Linear Fit')

    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('Amplitude(nA)')
    plt.title('Linear fitting of the ampltitude and piezo data')
    plt.legend()
    plt.show()


    # ----------------******************************* this is the final data we will save in .dat file .------------------
    ampdata2saveAspiezo_nm = xpiezo_nm[desired_nmBackIndexwrtoInflexion:data_choose_endindex]   # data_choose_endindex --> it is the last index = dataendamp 979 
    print(ampdata2saveAspiezo_nm.head())
    # ampdata2saveAspiezo_nm = ampdata2saveAspiezo_nm + c/m
    ampdata2saveAspiezo_nm = ampdata2saveAspiezo_nm - ampdata2saveAspiezo_nm[desired_nmBackIndexwrtoInflexion] 

    ampdata2saveAsAmplitude_nm = (1/m)* ampdf['Amplitude'][desired_nmBackIndexwrtoInflexion:data_choose_endindex]

    ampdata2saveAsAmplitude_nm.shape
    plt.plot(ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,'-r')
    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('Amplitude(nm)')
    plt.title('just to check before saving to .dat file')
    # plt.legend()
    plt.show()


    # #  this is for the phase values:---------------------------------********


    print(phasedf.iloc[0,1]) # first value added -- phasedf.iloc[0,1]
    # last value add ---- > phasedf.iloc[data_endamp-1,1] 

    phase  = - phasedf['Phase'] -90 + phasedf.iloc[data_endamp-1,1]
    print("\n", phase.shape)
    print("\n new phase values: \n", phase[0:5])

    phasedata2savedegree = phase[desired_nmBackIndexwrtoInflexion:data_choose_endindex]

    plt.plot(ampdata2saveAspiezo_nm,phasedata2savedegree,'-b')
    plt.grid()
    plt.xlabel('piezo(nm)')
    plt.ylabel('phase(o)')
    plt.title('PHASE in degree just to check before saving to .dat file')
    # plt.legend()
    plt.show()

# <----------------------------any data can select depend on the starting and ending points given in arguments or defined above. ---------------- >
    # <------------------ use these two as base and select any data part from this here phase in degree and ampdf in nm. ------------- >
    # ampdata2saveAsAmplitude_nm = (1/m)* ampdf['Amplitude']    # <---- in nm  
    # phasedata2savedegree = phase                              # <----- in degree 

    ampfrominflexion2flat_nm = (1/m)* ampdf['Amplitude'][index_inflexion:dataselect1]
    phasefrominflexion2flat_degree = phase[index_inflexion:dataselect1]
    piezofrominflexion2flat_nm  = ampdata2saveAspiezo_nm[index_inflexion:dataselect1]   # <--- this is the final data to save as piezo in nm.



    # # now generate a .dat file from the where data is saved ( unit: nm)
    return (ampdata2saveAspiezo_nm,ampdata2saveAsAmplitude_nm,phasedata2savedegree,ampfrominflexion2flat_nm,phasefrominflexion2flat_degree,piezofrominflexion2flat_nm)