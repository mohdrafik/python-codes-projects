import pandas as pd
import numpy as np 
def readASdfsetaxisAmpasnp(data_path): 

    # from inflexionMinimadownbump import findDownBump 
    # excel_path = "C:\\Users\\mrafik\\Desktop\\python_general_code\\xlsfileprocess\\"
#     excel_path = "E:\\python_programs\\xlsfileprocess\\dataproblem\\"
    # excel_path = "E:\\python_programs\\xlsfileprocess\\"
    excel_path = data_path
    filenameAmplitude = 'Amplitude40.xlsx'
    ampdf = pd.read_excel(excel_path+filenameAmplitude)
    ampdf = ampdf.set_axis(['Piezo','Amplitude'],axis='columns')
    print(ampdf.head(),"\n")
    #  ------------------------- phase -------------------- > 
    filenamephase = 'phase40.xlsx'
    phasedf = pd.read_excel(excel_path+filenamephase)
    phasedf = phasedf.set_axis(['Piezo','Phase'],axis='columns')
    print(phasedf.head(),"\n")
    print(ampdf.shape)
    # x= nm  , y= nA
    # <--------------------------- these two points are used later data_endamp and ampdfPiezoColumn  >
    data_endamp =ampdf.shape[0]
    print("end data points = \n",data_endamp)

    ampdfPiezoColumn = np.array(ampdf['Piezo'])
#     print()
    return (ampdf,phasedf,data_endamp,ampdfPiezoColumn)