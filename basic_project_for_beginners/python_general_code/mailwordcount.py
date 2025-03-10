with open('maildata1.txt', 'r') as f:
    # data = f.read()
    dline = f.readlines()

    # print(dline)
    # x =0
    # while(line = f.readline()):
    #     # d = data.readline()
    #     dlist=line.split(' ')
    #     count = len(dlist)
    #     x = x + count
    # print(x)
    count = 0
    sum = 0
    for line in dline:
        count += 1
        sline = line.split(' ')
        wcount = 0
        for word in sline:
            if  count ==3:
                pass
                print(word)

            wcount += 1
        print(wcount)    
        # print(line)
        
        sum = sum+wcount

print("no of lines = ", count)
print("total word count in mail = ",sum)
