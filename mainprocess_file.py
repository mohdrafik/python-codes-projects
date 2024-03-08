# import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio

from listxlsfilesinOrder import listxlsFiles
from converdfSetAxisgetNumpyArray import readASdfsetaxisAmpasnp


data_path =  "dataproblem\\"
amp_inOrder,Phase_inOrder = listxlsFiles(data_path)
print("in mian:",amp_inOrder,Phase_inOrder)
for i in range(len(amp_inOrder)):
    filenameAmplitude = amp_inOrder[i]
    filenamephase = Phase_inOrder[i]
    print(f"I am dealing with file = {i+1}.")
    readASdfsetaxisAmpasnp(data_path,filenameAmplitude,filenamephase) # it returns (ampdf (979,2),phasedf(979,2),data_endamp (no .of rows ),ampdfPiezoColumn (numpy array column of piezo value only. ))
    print(f"I have read and converted the data in dataframe and numpy array and no of row in amp as data_endamp for file {i+1} named as {filenameAmplitude} and {filenamephase}.")
    


