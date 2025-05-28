import numpy as np
# import matplotlib as matplotlib
# import matplotlib
# we can plot matplotlib, but it will import all function make slow. for while we can only import.
# matplotlib inline
import tight as tight
from matplotlib import pyplot as plt
from numpy import linspace

# plt.plot([1, 2, 3], [2, 4, 6])
# # plt.show()  if you write here it will not show title heading.
# plt.title("data")
# plt.xlabel("x data")
# plt.ylabel("y data")
# plt.show()
# from matplotlib import style

# style.use('ggplot')
x = linspace(0, 20)
y1 = 2.*x*x
y2 = 2.*x*x/2
# plt.plot(x, y1, x, y2, label='first',line-width ='2')
plt.scatter(x, y1, label='first')
# plt.hist(x, y2, label='second')
plt.xlim(min(x), max(x))
plt.ylim(min(min(y1), min(y2)), max(max(y1), max(y2)))
plt.grid()
plt.legend()
plt.show()

plt.hist(x, y2, label='second')
plt.show()