path = "C:\\Users\mrafik\\Desktop\\filepathname"
import os
for i in range(0,8,1):
    # dirpath = os.path.join(path)
    # os.makedirs(dirpath,"week"{i})
    filename = f"week{i}"
    os.makedirs(filename, exist_ok=True)
    print(f"week{i}")
    # %mkdir "week"{i}
