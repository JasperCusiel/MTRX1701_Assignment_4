import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def equation(l, x, y, c):
    c1, c2, c3, c4, c5, c6 = c
    return c1 * ((c2 * l) - (c3 * x) - c4) * np.exp(-c5 * l) + (c6 * y)


def plot_3d_surface(c):
    x = np.linspace(0, 50, 100)
    y = np.linspace(0, 25, 100)
    x, y = np.meshgrid(x, y)
    l = 1 / (y + 0.08 * x) - (0.035) / ((x ** 3) + 1)
    z = equation(l, x, y, c)
    z = np.clip(z, 0, 0.5)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='bone')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 25)
    ax.set_zlim(0, 0.5)

    plt.show()


c = [0.5176, 116, 0.4, 5, 21, 0.0068]
plot_3d_surface(c)
