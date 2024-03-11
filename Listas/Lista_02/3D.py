# Plotagem de gráfico 3D em python com matplotlib

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection="3d")
x=[0,1,2,3,4,5,6]
y=[0,1,4,9,16,25,36]
z=[0,1,4,9,16,25,36]
ax.plot3D(x, y, z, 'red')
ax.scatter3D(x, y, z, c=z, cmap='cividis');
plt.show()
