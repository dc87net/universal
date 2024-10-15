import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, gamma, cos, pi, mp
from scipy.fft import fft2, fftshift

# Set precision
mp.dps = 25

# Compute values using our symbolic method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Define the range for the parameter t
t_values = np.linspace(0, 100, 2000)

# Compute zeta function values
zeta_vals = np.array([complex(zeta_symbolic(t)) for t in t_values])
print(f"Zeta Values:\n")
print(f"{zeta_vals}")
real_parts = np.real(zeta_vals)
imag_parts = np.imag(zeta_vals)

# Create a 2D array combining real and imaginary parts
data = np.vstack((real_parts, imag_parts))

# Perform 2D Fourier Transform
fft_result = fft2(data)
fft_magnitude = np.abs(fftshift(fft_result))

# Plot the heat map of the Fourier transform magnitude
plt.figure(figsize=(10, 8))
# plt.imshow(fft_magnitude, extent=[-np.pi, np.pi, -np.pi, np.pi], cmap='nipy_spectral', aspect='auto')
plt.imshow(fft_magnitude, extent=[-np.pi, np.pi, -np.pi, np.pi], cmap='seismic', aspect='auto')
plt.colorbar(label='Magnitude')
plt.title('2D Fourier Transform of the Top-Down Projection of the Symbolic Riemann Zeta Function')
plt.xlabel('Frequency (Real Part)')
plt.ylabel('Frequency (Imaginary Part)')
plt.show()
