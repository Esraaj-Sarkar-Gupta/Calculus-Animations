# Animated plot of x and f(x)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#%matplotlib qt
#%matplotlib inline

fig, ax = plt.subplots()
xdata, ydata0, ydata1 = [], [], []
ln0, = plt.plot([], [], 'r', animated=True)
ln1, = plt.plot([], [], 'b', animated=True)
x1 = np.linspace(0, 3, 200)
#x = reversed(x1)
x = x1

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 9)
    ln0.set_data(xdata,ydata0)
    ln1.set_data(xdata,ydata1)
    return ln0, ln1

def update(x):
    xdata.append(x)
    ydata0.append(0*x)
    ydata1.append(x**2)
    ln0.set_data(xdata, ydata0)
    ln1.set_data(xdata, ydata1)
    return ln0, ln1,

ani = FuncAnimation(fig, update, frames=x,
                    init_func=init, blit=True, interval=80, repeat=True)
plt.grid()
ani.save("./Test.gif")
plt.show()