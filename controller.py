import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm
import true_wave_function as tw


def coefficient_of_performance(x_val, blade_pitch):
    # Calculates y value (coefficient_of_performance) as a function of the x_value (lambda) and blade pitch

    one_over_lambda_i = (1 / (x_val + 0.08 * blade_pitch)) - (0.035 / (pow(blade_pitch, 3) + 1))

    y_val = 0.5176 * ((116 * one_over_lambda_i) - (0.4 * blade_pitch) - 5) * math.exp(-21 * one_over_lambda_i) + (
            0.0068 * x_val)

    return y_val


def random_wave_function(t):
    ws = 10
    result = []
    for _ in t:
        result.append(ws)
        ws += np.random.normal(scale=0.8)
        ws = max(min(ws, 20), 1)
    return result


if __name__ == '__main__':
    # Random wind speed seed
    np.random.seed(328808)

    # Subplot axes label settings
    label_font_size = 8

    # Plot setup
    fig = plt.figure()

    # Add subplots with gridspec
    gs = fig.add_gridspec(4, 2)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[2, 0])
    ax4 = fig.add_subplot(gs[3, 0])
    ax5 = fig.add_subplot(gs[0:, 1])

    # Add grid lines to plots
    ax1.grid()
    ax2.grid()
    ax3.grid()
    ax4.grid()

    # Optimisation plot setup
    ax5.set_title('Optimal Pitch Angle Function For a Given Lambda', pad=20)
    ax5.set_ylabel("Cp, Coefficient of Performance", rotation=90, fontsize=label_font_size)
    ax5.set_xlabel("Beta, Blade Pitch", fontsize=label_font_size)
    ax5.set_xlim([0, 20])
    ax5.set_ylim([-0.1, 0.5])

    # Time axis setup
    time = np.arange(0, 100, 1)

    # Generate random wind data
    wind_data = random_wave_function(time)

    # Calculation variables
    rotor_speed = 0
    previous_rotor_speed = 0
    previous_lambda = 8.1
    previous_wind_speed = 10


    # For tracking variable history over time
    variable_pitch_angle_history = []
    rotor_speed_history = []

    # Generate a range of pitch angles between the max and min pitch angle
    beta = np.linspace(0, 20, 50)

    cp_varibale_pitch = []

    fixed_beta = 1
    fixed_beta_over_time = np.full(shape=len(wind_data), fill_value=fixed_beta)
    cp_fixed_pitch = []
    plotted_lambdas = []  # Keep track of lambdas that are already plotted to avoid double ups

    # Normalize your lambda values to range [0,1] for the colormap
    norm = plt.Normalize(0, 18)
    cmap = cm.plasma
    fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax5)

    for wind_speed in wind_data:



        lambda_val = wind_speed * previous_lambda / previous_wind_speed
        rotor_speed = wind_speed / previous_lambda

        rotor_speed_history.append(previous_rotor_speed)

        # Coefficient of performance calculations
        cp_for_given_pitch_angle = []

        # Variable pitch optimization
        for b in beta:
            cp_for_given_pitch_angle.append(coefficient_of_performance(lambda_val, b))

        # Fixed pitch angle
        cp_fixed_pitch.append(coefficient_of_performance(lambda_val, fixed_beta))

        # Variable Pitch Angle
        if not (round(lambda_val, 2) in plotted_lambdas):
            ax5.plot(beta, cp_for_given_pitch_angle, label=round(lambda_val, 2), color=cmap(norm(lambda_val)))
            plotted_lambdas.append(round(lambda_val, 2))

        # Find pitch angle
        highest_cp = max(cp_for_given_pitch_angle)
        corresponding_pitch_angle = float(beta[cp_for_given_pitch_angle.index(highest_cp)])

        variable_pitch_angle_history.append(corresponding_pitch_angle)
        cp_varibale_pitch.append(highest_cp)

        #ax5.plot(corresponding_pitch_angle, highest_cp, 'ro', label="beta = {}".format(round(corresponding_pitch_angle, 2)))

        previous_lambda = lambda_val
        previous_rotor_speed = rotor_speed
        previous_wind_speed = wind_speed

    # Variable Pitch Angle over time
    ax4.plot(time, variable_pitch_angle_history, label='Variable Pitch')

    # Fixed Pitch angle
    ax4.plot(time, fixed_beta_over_time, color='red', label='Fixed Pitch')

    ax4.set_ylabel("Blade Pitch Angle (deg)", rotation=0, fontsize=label_font_size, labelpad=50)
    ax4.legend(fontsize=7)


    ax1.plot(time, wind_data)
    ax1.set_ylabel("Wind Speed (m/s)", rotation=0, fontsize=label_font_size, labelpad=50)
    ax1.set_title('Variable Vs Fixed Blade Pitch Control \nPerformance For A Given Wind Speed', pad=15)

    # Variable Pitch performance
    ax3.plot(time, cp_varibale_pitch, label='Variable Pitch')

    # Fixed Pitch performance
    ax3.plot(time, cp_fixed_pitch, color='red', label='Fixed Pitch')
    ax3.set_ylabel("Cp, Coefficient\n of Performance", rotation=0, fontsize=label_font_size, labelpad=50)
    ax3.legend(fontsize=7)

    ax2.plot(time, rotor_speed_history)
    ax2.set_ylabel("Rotor Speed, Rad/s", rotation=0, fontsize=label_font_size, labelpad=50)
    ax4.set_xlabel("Time (arbitrary unit)", fontsize=label_font_size)

    plt.show()
