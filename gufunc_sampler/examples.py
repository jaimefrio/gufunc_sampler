from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import gufunc_sampler as gs

# Mandelbrot set
rows = np.linspace(-1.25, 1.25, 1250)
cols = np.linspace(-2, 0.5, 1250)

mandel_set = gs.mandelbrot(cols + 1.j * rows[:, np.newaxis], 50)
plt.subplot(121)
plt.imshow(mandel_set, interpolation='nearest', cmap='hot')
                                                                                                                                                                                                                                                                                                                                                                                                 
# Point in polygon
points = np.random.rand(1000, 2)
triangle = np.random.rand(5, 2)
inside = gs.point_in_polygon(triangle[:, 0], triangle[:, 1],
                             points[:, 0], points[:, 1])
points_in = points[inside]
points_out = points[~inside]
plt.subplot(122, aspect='equal')
triangle = np.vstack((triangle, triangle[0]))
plt.plot(triangle[:, 0], triangle[:, 1], 'k-')
plt.plot(points_in[:, 0], points_in[:, 1], 'bx')
plt.plot(points_out[:, 0], points_out[:, 1], 'rx')
