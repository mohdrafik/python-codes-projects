import matplotlib.pyplot as plt
import numpy as np

x1 = [1,4,6,8]
y1=[1,10,100,1000]
plt.figure(figsize=(16,9))
plt.plot(x1,y1,'-sr')
plt.title('exp')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.tight_layout
plt.show()

