import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

fig = plt.figure()
ax = plt.gca()  # Get current axis

l, = plt.plot([],[],'r-')

plt.xlim(-1,1)
plt.ylim(-4,4)

def fun(x):
    return np.sin(10*x)*3

# xlist = np.linspace(-5,5,100)
# ylist = fun(xlist)

# l.set_data(xlist,ylist)
# plt.show()

xlist = []
ylist = []

metadata = dict(title='gif_Movie',artist = 'Moh_Rafik')
writer = PillowWriter(fps = 15, metadata= metadata)

with writer.saving(fig,"sinWave.gif",100):
    for xval in np.linspace(-1,1,100):
        xlist.append(xval)
        ylist.append(fun(xval))
        l.set_data(xlist,ylist)

        writer.grab_frame()

plt.show()
