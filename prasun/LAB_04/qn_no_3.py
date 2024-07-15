#Consider a sine wave with frequency 3hz, amplitude 1 and phase 0. Generate 10 different samples from the sine wave at interval of 0.3 starting from 0sec. Plot the samples against time using python matplotlib.
import numpy as np
import matplotlib.pyplot as plt

# Sine wave parameters
freq = 3
amplitude = 1
phase = 0
interval = 0.3
samples = 10

# Generate time samples
time_samples = np.arange(0, samples * interval, interval)
sine_wave_samples = amplitude * np.sin(2 * np.pi * freq * time_samples + phase)

# Plot the samples
plt.figure(figsize=(10, 4))
plt.plot(time_samples, sine_wave_samples, 'o-', label='Samples')
plt.title('Sine wave samples at intervals of 0.3s')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.show()