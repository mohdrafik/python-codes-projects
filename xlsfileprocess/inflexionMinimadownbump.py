import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import matplotlib.pyplot as pyplot
# df = pd.read_excel('Amplitudexls.xlsx')
# # print(df.head())
# dataendpoint =320
# df.set_axis(['Piezo','Amplitude'],axis = 'columns' )
# ampdf = df

def findDownBump(ampdf, zero_orFlatAmp):
    
    ampdfAmplitudeColumn = np.array(ampdf['Amplitude'])
    slicingStartIndex = 4
    ampdfAmplitudeColumn = ampdfAmplitudeColumn[slicingStartIndex:zero_orFlatAmp]
    print(" the shape and size of the amplitude array before the np.diff: (4:dataendpoint) \n",ampdfAmplitudeColumn.shape)
    y = ampdfAmplitudeColumn

    x = ampdf['Piezo'][4:zero_orFlatAmp]
    print("x values\n and shape of x ",x[0:5], x.shape)
    x = np.array(x)
    arr =  np.diff(ampdfAmplitudeColumn)

    print("I am indsid ethe array: function arary \n:",arr[0:10])
    neg_indices = np.where(arr < 0)[0]  # Find where the array is negative

     
    if len(neg_indices) == 0:    # If there are no negative values, return an empty array
        return np.array([])

    # Find the consecutive differences of indices
    diff = np.diff(neg_indices)

    # Find where the differences are not equal to 1
    diff_not_1 = np.where(diff != 1)[0]

    split_indices = np.split(neg_indices, diff_not_1 + 1)  # Split the indices into consecutive sequences

    lengths = np.array([len(seq) for seq in split_indices])     # Find the length of each consecutive sequence
    max_length_index = np.argmax(lengths)      # Find the index of the longest consecutive sequence

    longest_sequence = split_indices[max_length_index]   # Get the longest consecutive sequence

    print("longest sequence =\n",longest_sequence)  #longest consecutive negative going sequence index value we get here
    # x = list(range(len(arr)))
    print("x axis=\n",x[longest_sequence])

    print("scat val x: \t \n",longest_sequence[0])

    # xscat = longest_sequence[0]    
    xscat  = x[longest_sequence[0]]   # it returns the indecx values for the minima starting points array

    print("scat val y: \t \n",arr[longest_sequence][0])
    # yscat = arr[[longest_sequence][0]]

    yscat = y[longest_sequence[0]]

    plt.plot(x,y,'.b')
    plt.scatter(xscat,yscat,color='red',marker= 'o',s = 100 ,label='Decreasing Points') # s=100, marker='o'
    plt.scatter(x[longest_sequence[-1]+1 ],y[longest_sequence[-1] +1],s = 90,color='red',marker= '*',label='Decreasing Points')  
    plt.xlabel('Piezo')
    plt.ylabel('Amplitude')
    plt.title('Circle:inflexion point, Star: Minima Point ')
    plt.grid()

    plt.show() 

    plt.close()

    ActualInflexionPointActualRawDataIndex = longest_sequence[0] + slicingStartIndex
    ActualMinimaPointActualRawDataIndex  = longest_sequence[-1] + slicingStartIndex + 1
    
    InflexionAfterSliceIndex = longest_sequence[0] 
    MinimaPointAfterSliceIndex  = longest_sequence[-1] +  1
    # plt.show()

    result = (ActualInflexionPointActualRawDataIndex , ActualMinimaPointActualRawDataIndex, InflexionAfterSliceIndex, MinimaPointAfterSliceIndex)
    print("\n Actual inflexion point Index with original data :  ", result[0],
          " \n Actual Minima point Index before Slicing with original Data : ", result[1],
            "\n inflexion point index after slicing: ", result[2],
        "\n Minima point Index After slicing: ",result[3])


    return (ActualInflexionPointActualRawDataIndex , ActualMinimaPointActualRawDataIndex, InflexionAfterSliceIndex, MinimaPointAfterSliceIndex)
    


if __name__=="__main__":
    excel_path = "C:\\Users\\mrafik\\Desktop\\python_general_code\\xlsfileprocess\\"
    ampdf = pd.read_excel(excel_path+'Amplitudexls.xlsx')
    ampdf= ampdf.set_axis(['Piezo','Amplitude'], axis ='columns')

    # df = pd.read_excel('Amplitudexls.xlsx')
    # # print(df.head())
    # # dataendpoint = 320
    # df = df.set_axis(['Piezo','Amplitude'],axis = 'columns')
    # ampdf = df
    # print(ampdf.head())
    zero_orFlatAmp = 322

    res = findDownBump(ampdf, zero_orFlatAmp)
    print("\n Actual inflexion point Index with original data :  ", res[0],
          " \n Actual Minima point Index before Slicing with original Data : ", res[1],
            "\n inflexion point index after slicing: ", res[2],
        "\n Minima point Index After slicing: ",res[3])
    
