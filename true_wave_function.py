def random_wave_function(time):
    base_level = 10
    noise_scale = 0.2
    amplitude1 = np.random.randint(1,4)
    amplitude2 = np.random.randint(1,4)
    frequency1 = np.random.rand()
    frequency2 = np.random.rand()
    phase_shift = np.pi / 4

    result = []
    for t in time:
        wave_value = (base_level +
                      amplitude1 * np.sin(frequency1 * t) +
                      amplitude2 * np.cos(frequency2 * t + phase_shift))
        noise = np.random.normal(scale=noise_scale)
        noisy_wave_value = wave_value + noise
        noisy_wave_value = max(min(noisy_wave_value, 20), 5)
        result.append(noisy_wave_value)
    
    return np.array(result)
