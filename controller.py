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
    ax.set_xlabel("beta")
    ax.set_xlim([0, 20])
    ax.set_ylim([-0.1, 0.5])


    #wind_speed = int(input("Wind Speed: "))
    rotor_speed = 1
    #lambda_val = 12/rotor_speed
    lambda_val = 10.75
    # Plot x, y values for a given pitch angle, beta
    beta = np.linspace(0, 20, 50)
    y = []

    for b in beta:
        y.append(coefficient_of_performance(lambda_val, b))

    ax.plot(beta, y, label="lambda = {}".format(lambda_val))

    max_y = max(y)
    max_x = float(beta[y.index(max_y)])
    ax.plot(max_x, max_y, 'ro', label="beta = {}".format(round(max_x, 2)))



    ax.legend()

    plt.show()

