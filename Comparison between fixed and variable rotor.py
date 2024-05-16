import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

def equation(l, x, y, c):
    c1, c2, c3, c4, c5, c6 = c
    result = c1 * ((c2 * l) - (c3 * x) - c4) * np.exp(-c5 * l) + (c6 * y)
    result = np.where(np.isclose(x, 0), 1e-10, result)
    return result

def generate_meshgrid():
    x = np.linspace(0, 50, 100)
    y = np.linspace(0, 25, 100)
    return np.meshgrid(x, y)

def compute_l(x, y):
    return 1/(y+0.08*x+1e-10)-(0.035)/((x**3)+1)

def clip_z_values(z):
    return np.clip(z, 0, 0.5)

def find_nan_indices(max_z_values):
    nan_index = np.where(np.isnan(max_z_values))[0]
    if nan_index.size > 0:
        max_z_values = max_z_values[nan_index[0]+1:]
    return max_z_values

def plot_3d_surface(x, y, z, max_z_values):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='hot')

    ax.plot(x[:,0], y[:,0], max_z_values, color='r', label='Maximum z-value')

    area_under_curve = simps(max_z_values, y[:,0])
    print("Area under the curve:", area_under_curve)

    ax.set_xlabel('Beta')
    ax.set_ylabel('Lambda')
    ax.set_zlabel('Coefficient of Performance')

    ax.set_xlim(0, 50) 
    ax.set_ylim(0, 25)
    ax.set_zlim(0, 0.5) 

    plt.legend()
    plt.title(f'Area under the curve: {area_under_curve}')
    plt.show()

def main():
    c = [0.5176, 116, 0.4, 5, 21, 0.0068]
    x, y = generate_meshgrid()
    l = compute_l(x, y)

    if np.any(np.isnan(l)) or np.any(np.isinf(l)):
        print("Warning: NaN or Inf encountered in 'l'.")

    z = equation(l, x, y, c)
    z = clip_z_values(z)

    max_z_values = np.max(z, axis=1)
    max_z_values = find_nan_indices(max_z_values)

    plot_3d_surface(x, y, z, max_z_values)

    # Create the second graph
    plt.figure()
    max_area = -np.inf
    max_area_beta = None

    for beta in np.linspace(0, 50, 100):
        yz_values = np.zeros_like(y[:, 0])

        for i, y_val in enumerate(y[:, 0]):
            yz_values[i] = equation(compute_l(beta, y_val), beta, y_val, c)

        area_under_curve = simps(yz_values, y[:, 0])
        if area_under_curve > max_area:
            max_area = area_under_curve
            max_area_beta = beta

        plt.plot(y[:, 0], yz_values, label=f'Beta={beta:.2f}, Area={area_under_curve:.2f}')

    plt.xlabel('Lambda')
    plt.ylabel('Cp')
    plt.title(f'Area under the yz curve: {max_area:.2f}')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Beta value where the area is greatest:", max_area_beta)

if __name__ == "__main__":
    main()

