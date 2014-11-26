#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)

plt.subplot(1, 2, 1)
# Plot the rectangular coordinates here
y_sin = np.sin(x)
y_sin2 = np.sin(x) * np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, 'r')
plt.plot(x, y_sin2, 'g')
plt.plot(x, y_cos, 'b')

plt.show()

plt.subplot(1, 2, 2, polor = True)
# Plot the polar coordinates here
