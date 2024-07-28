import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import math
import os

"""
give you datapath only program will process all files one by one.. 
I think the hamaker in joule, give you datapath 
K= 26.90  # N/m
Q= 466
R = 10  #nm
Piezo Amp near distant in meter

"""
def hamaker_const(datapath,filename):
    # df_nd = pd.read_excel('408 with neardistance.xlsx')
    # df_nd = pd.read_excel("408 with piezo.xlsx")
    file2read = os.path.join(datapath,filename)

    df_nd = pd.read_excel(file2read)
    for col in df_nd.columns:
        print(col)
        if col =="piezo":
            distancekey = "piezo"
        elif col == "piezo ":
            distancekey = "piezo "
        elif col == "neardistance ":
            distancekey = "neardistance "
        elif  col == "neardistance":
            distancekey = "neardistance"
        else:
            print("----------- May be new key is there just check :----->")
            

    print(df_nd.head() ,"and size:\n ",df_nd.shape,"\n", df_nd.tail(),"\n")   # Piezo Amp near distant in meter
    K= 26.90  # N/m
    Q= 466
    R = 10  # nm 
    R = R*1e-9  # m now after convert from nm 
    A0 = df_nd['amplitude'].iloc[-1]
    K_constant = -(3*K*A0)/(Q*R)

    phase_deg = df_nd["phase"]
    df_nd["phase_radian"] = np.deg2rad(df_nd["phase"])

    # cosphi = [ math.cos(phase) for phase in df_nd['phase']]  # when by default phase in degree
    # phase_radians = [math.radians(phase) for phase in df_nd['phase']]  # here phase converted to radian
    # cosphi_rad = [ math.cos(phase) for phase in phase_radian]
    # cos_phi_rad = np.cos(phase_radian)
    cos_phi_rad = np.cos(df_nd["phase_radian"])
    cos_phi_deg = np.cos(phase_deg)
    print(f"A_cosphi \n:{cos_phi_rad}  and\n  --> Phase in radians: \n {1},\n {phase_deg} \n {df_nd} ")
    Asqu_multi_cosphi = df_nd['amplitude']**2 *cos_phi_rad   # Asqu_multi_cosphi = df_nd['amplitude']**2 *(cos_phi_rad)
    # last_term = ((df_nd["neardistance"]/df_nd["amplitude"] + 1)**2  - 1 )**1.5
    last_term = ((df_nd[distancekey]/df_nd["amplitude"] + 1)**2  - 1 )**1.5

    ham_cons = K_constant * Asqu_multi_cosphi*last_term  # hm = - (3 * k * A0 * A**2 * math.cos(phi) / (Q * R)) * (((d + A) / A)**2 - 1)**(3/2)
    df_nd["ham_const"] = ham_cons
    ham_cons_avg = np.mean(ham_cons)
    df_nd["ham_cons_avg"] = ham_cons_avg

    print(f"ham constant :{ham_cons} and \n{ham_cons.shape} and \n \n ----> hawmaker average value:\n {ham_cons_avg}")
    ham_consfilename = "hamaker_data"+filename[0:-5]+".xlsx"
    ham_consfilenamefinal = os.path.join(datapath,ham_consfilename)
    df_nd.to_excel(ham_consfilenamefinal)

    res = {
            "filename":filename[0:-5],
            "hamaker_const":ham_cons_avg
           }
    return res
    # df_nd2 = df_nd['amplitude'] -(1.65*ones_array) 
    # print("df2: ",df_nd2.head())
    # plt.figure()
    # plt.subplot(2,1,1)
    # plt.plot(df_nd['neardistance'], df_nd['amplitude'] -(1.65e-8) )  
    # plt.grid(True)
    # plt.subplot(2,1,2)
    # plt.plot(df_nd['neardistance'], df_nd['amplitude']) 
    # plt.grid(True)
    # # plt.plot(df_nd['neardistance'],df_nd['phase'])
if __name__=="__main__":
    
    filename_list = []
    hamaker_constavglist = []

    datapath = "E:\\python_programs\\xlsfileprocess\\hamaker_data\\"
    for filename in os.listdir(datapath):
        print("<------------------------------->",filename,)
        if filename[-5:] ==".xlsx" and filename[0:7] !='hamaker':
            print(f" current processing file name is {filename}") 
            result = hamaker_const(datapath,filename)

            filename_list.append(result["filename"])
            hamaker_constavglist.append(result["hamaker_const"])

    hamaker_constavgData = {"filename":filename_list,"hammaker_constant":hamaker_constavglist }

    hamaker_constavgData_df = pd.DataFrame(hamaker_constavgData)

    hamaker_constavgData_df.to_excel(os.path.join(datapath,'hamaker_avgValeachfile.xlsx'))        

