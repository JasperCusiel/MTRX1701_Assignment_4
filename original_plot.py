import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import math


def cp(lambda_val, pitch_angle):
    # Coefficients for the cp calculation
    c1 = 0.5176
    c2 = 116
    c3 = 0.4
    c4 = 5
    c5 = 21
    c6 = 0.0068

    # Calculate 1/lambda_i
    one_over_lambda_i = (1 / (lambda_val + 0.08 * pitch_angle)) - (0.035 / ((pow(pitch_angle, 3) + 1)))

    # Calculate cp
    cp_val = c1 * ((c2 / one_over_lambda_i) - (c3 * pitch_angle) - c4) * math.exp(-c5 / one_over_lambda_i) + (c6 * lambda_val)

    return cp_val


def wind_turbine_model(wind_speed, generator_speed, pitch_angle, wind_base, lambda_nom, cp_nom):
    # Avoid division by zero
    if wind_speed == 0 or generator_speed == 0:
        return None

    # Convert wind speed to per unit (pu)
    wind_speed_pu = wind_speed * (wind_speed / wind_base)

    P_wind_pu = pow(wind_speed_pu, 3)

    lambda_pu = generator_speed/wind_speed_pu

    lambda_val = (lambda_pu * lambda_nom)

    # Calculate power coefficient, cp
    cp_val = cp(lambda_val, pitch_angle)

    cp_pu = (cp_val/cp_nom)


    Pm_pu = (P_wind_pu * cp_pu)

    Tm_pu = (Pm_pu/generator_speed)

    return Tm_pu


if __name__ == '__main__':
    plt, ax = plt.subplots()
    wind_speeds = [6, 7.2, 8.8, 9.6, 10.8, 12, 13.2, 14.4]
    generator_speeds = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4]

    a = []
    for i in range(len(wind_speeds)):
        a.append(wind_turbine_model(wind_speeds[i], generator_speeds[i], 0, 12, 8.1, 1.2))

    print(a)

    ax.scatter(generator_speeds, a)
    plt.show()