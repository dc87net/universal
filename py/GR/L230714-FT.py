import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fftn, fftshift

# Parameters
V0 = 1.0  # Depth of the potential well
k = 1.0   # Determines the width of the well
x = np.linspace(-10, 10, 400)
t = np.linspace(0, 10, 400)
X, T = np.meshgrid(x, t)

# Wave function (example, real and imaginary parts)
psi_real = np.exp(-0.5 * (X ** 2 + T ** 2)) * np.cos(2 * np.pi * X)
psi_imag = np.exp(-0.5 * (X ** 2 + T ** 2)) * np.sin(2 * np.pi * X)
psi = psi_real + 1j * psi_imag

# Perform 2D Fourier Transform
psi_freq = fftn(psi)
psi_freq_shifted = fftshift(psi_freq)  # Shift zero frequency to center

# Frequency axes
kx = np.fft.fftfreq(x.size, x[1] - x[0])
kt = np.fft.fftfreq(t.size, t[1] - t[0])
KX, KT = np.meshgrid(fftshift(kx), fftshift(kt))

# Plotting the frequency domain
fig = plt.figure(figsize=(14, 6))

# Magnitude of the frequency components
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(KX, KT, np.abs(psi_freq_shifted), cmap='turbo')
ax1.set_title('Magnitude of Frequency Components')
ax1.set_xlabel('Spatial Frequency (kx)')
ax1.set_ylabel('Temporal Frequency (kt)')
ax1.set_zlabel('Magnitude')

# Phase of the frequency components
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(KX, KT, np.angle(psi_freq_shifted), cmap='rainbow_r')
ax2.set_title('Phase of Frequency Components')
ax2.set_xlabel('Spatial Frequency (kx)')
ax2.set_ylabel('Temporal Frequency (kt)')
ax2.set_zlabel('Phase')

plt.show()