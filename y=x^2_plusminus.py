# Function y = x^2 as x ->0+ and x -> 0-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
X_pos, X_neg, Y0_pos, Y0_neg, Y_pos, Y_neg = [], [], [], [], [], [] # Initialise value lists

ln_pos, = plt.plot([], [], color = 'red', animated = True)
ln0_pos, = plt.plot([], [], color = 'purple' , animated = True)

ln_neg, = plt.plot([], [], color = 'blue', animated = True)
ln0_neg, = plt.plot([], [], color = 'purple', animated = True)

x_pos = reversed(np.linspace(0, 3, 200))
x_neg = np.linspace(-3, 0, 200)

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 9)
    
    ln_pos.set_data(X_pos, Y_pos)
    ln0_pos.set_data(X_pos, Y0_pos)
    
    ln_neg.set_data(X_neg, Y_neg)
    ln0_neg.set_data(X_neg, Y0_neg)
    
    return ln_pos, ln0_pos, ln_neg, ln0_neg

def update(frame):
    x_pos = frame
    x_neg = -frame
    
    X_pos.append(x_pos)
    X_neg.append(x_neg)
    
    Y0_pos.append(0)
    Y0_neg.append(0)
    
    Y_pos.append(x_pos**2)
    Y_neg.append(x_neg **2)
    
    ln_pos.set_data(X_pos, Y_pos)
    ln0_pos.set_data(X_pos, Y0_pos)
    
    ln_neg.set_data(X_neg, Y_neg)
    ln0_neg.set_data(X_neg, Y0_neg)
    
    return ln_pos, ln0_pos, ln_neg, ln0_neg


animation = FuncAnimation(fig, update, frames = np.linspace(0, 3, 200)[::-1], init_func = init, interval = 80, blit = True, repeat = True)
    
plt.grid(True)
animation.save("./y=x2_limits.gif")
print('Animation saved!')
plt.close()
    