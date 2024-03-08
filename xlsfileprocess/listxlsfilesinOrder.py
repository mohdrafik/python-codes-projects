import os
data_path =  "dataproblem\\"
def listxlsFiles(data_path):
    listOfFiles = os.listdir(data_path)
    # print(listOfFiles)
    amp_seperate_list = []
    phase_seperate_list = []
    for file in listOfFiles:
        if file[-5:] =='.xlsx':
            if file[0:9] =="Amplitude":
                print("amplitude:",file[9:-5])
                num_Subscript = file[9:-5]
                amp_seperate_list.append(file)
                for file in listOfFiles:
                    if file[0:5] == "phase" and num_Subscript == file[5:-5]:
                        print("for pahse:",file[5:-5])
                        phase_seperate_list.append(file)
    print("\n",amp_seperate_list,"\n length of the amp list -->",len(amp_seperate_list))
    print("\n",phase_seperate_list,"\n length of the phase list -->",len(phase_seperate_list))
    l1= amp_seperate_list
    l2= phase_seperate_list
    return l1,l2
if __name__=="__main__":
    data_path =  "dataproblem\\"
    listxlsFiles(data_path)