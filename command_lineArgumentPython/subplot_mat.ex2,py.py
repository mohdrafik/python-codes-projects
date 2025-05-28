from matplotlib import pyplot as plt
import numpy as np

x1 = np.linspace(1, 10)
list1 = ['rs', 'y^', 'b*', 'm+']
list2 = ['1', '2', '3', '4']
for i in range(0, 4):
    var1 = list1[i]
    plt.subplot(2, 2, i + 1)
    plt.plot(x1, (i + 1) * x1, var1 + '-')
    plt.xlabel('x data' + list2[i])
    plt.ylabel('y data ' + list2[i])
    plt.title(' plot ' + list2[i])

plt.show()
