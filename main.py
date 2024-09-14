import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#fig and axes
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'b', animated=True)

def init():
    ax.set_xlim(0, 2 * np.pi) #set x-axis limit
    ax.set_ylim(-1, 1) #Set y-axis limit
    ax.grid(True) #add grid lines
    ln.set_data([], [])
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.cos(frame))
    if len(xdata) > 50:
        xdata.pop(0)
        ydata.pop(0)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True, interval=50)

plt.show()
