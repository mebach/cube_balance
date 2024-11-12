 # THINGS TO DO
# Change data plotter to hold the the new state variables, not just z position but a z and theta
# Have animation draw new box

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../..')  # add parent directory
import cubeParam as P
from signalGenerator import signalGenerator
from cubeAnimation import cubeAnimation
from dataPlotter import dataPlotter
from cubeDynamics import cubeDynamics
from cubeController import cubeController

# instantiate reference input classes
reference = signalGenerator(amplitude=np.acos(np.sqrt(3)/3)/2, frequency=1, y_offset=np.acos(np.sqrt(3)/3)/2)
torque = signalGenerator(amplitude=0.0, frequency=0.001)
noise = signalGenerator(amplitude=0.01, frequency=0.001)
cube = cubeDynamics(alpha=0.0)
controller = cubeController()

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = cubeAnimation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop

    # Propate dynamics at rate Ts
    t_next_plot = t + P.t_plot
    while t < t_next_plot:
        # r = P.des_state
        # r[0] = reference.sin(t)
        n = 0 # noise.random(t)  # simulate sensor noise
        # x = cube.state + n
        # u = controller.update(r, x)
        # y = cube.update(u)
        t = t + P.Ts

    # update animation
    animation.update([reference.sin(t), reference.sin(t), reference.sin(t)])
    # dataPlot.update(t, r.item(0), cube.state, u)

    #plt.show()
    t = t + P.t_plot  # advance time by t_plot
    plt.pause(0.0001)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
