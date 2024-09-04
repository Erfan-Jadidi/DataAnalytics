import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

X = [100, 110, 190, 200, 220, 300, 320, 350, 400, 420]
y = [80, 100, 160, 170, 250, 265, 330, 340, 370, 400]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

line1, = ax1.plot(np.arange(1000), np.random.randint(1,100,1000), color='black')
line2, = ax2.plot(np.arange(1000), np.random.randint(1,100,1000), color='black')


def animate(i):
    # line1, = ax1.plot(np.random.randint (1, 100,1000), color='black')
    line2, = ax2.plot(np.random.randint(1,100,1000), color='black')
    return [line1, line2]


ani = FuncAnimation(fig, animate, frames=100, interval=1000)
plt.show()
