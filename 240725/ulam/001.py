import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Define the Zeta function (simplified for demonstration)
def zeta_function(x, y):
    return np.sin(x) + 1j * np.cos(y)

# Sample the function
x = np.linspace(0, 50, 500)
y = np.linspace(0, 50, 500)
zeta_values = zeta_function(x, y)

# Perform Fourier Transform
zeta_fft = fft(zeta_values)

# Plot the results
plt.figure(figsize=(12, 6))

# Plot magnitude of FFT
plt.subplot(121)
plt.plot(np.abs(zeta_fft))
plt.title('Magnitude of FFT of Zeta Function')

# Plot phase of FFT
plt.subplot(122)
plt.plot(np.angle(zeta_fft))
plt.title('Phase of FFT of Zeta Function')

plt.show()