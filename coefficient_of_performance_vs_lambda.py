import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

matplotlib.use('TkAgg')


def coefficient_of_performance(x_val, blade_pitch):
    # Calculates y value (coefficient_of_performance) as a function of the x_value (lambda) and blade pitch

    one_over_lambda_i = (1 / (x_val + 0.08 * blade_pitch)) - (0.035 / (pow(blade_pitch, 3) + 1))

    y_val = 0.5176 * ((116 * one_over_lambda_i) - (0.4 * blade_pitch) - 5) * math.exp(-21 * one_over_lambda_i) + (
            0.0068 * x_val)

    return y_val


if __name__ == '__main__':
    # Plot setup
    plt, ax = plt.subplots()
    ax.set_ylabel("Cp, Coefficient of Performance")
    ax.set_xlabel("Lambda, Tip speed ratio of the rotor blade tip speed to wind speed")
    ax.set_xlim([0, 15])
    ax.set_ylim([-0.1, 0.5])


    # Blade pitch angles
    beta_vals = np.linspace(0, 20, 5)

    for b in beta_vals:
        # Plot x, y values for a given pitch angle, beta
        x = np.linspace(0, 15, 50)
        y = []

        for i in x:
            y.append(coefficient_of_performance(i, b))

        ax.plot(x, y, label="{} degrees".format(b))
    ax.legend()
    plt.show()
