import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fftn, fftshift, ifftn
from mpl_toolkits.mplot3d import Axes3D

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

# Define filters
def apply_filter(freq_data, filter_func):
    return filter_func(freq_data)

def high_pass_filter(data, threshold):
    mask = np.abs(data) > threshold
    return data * mask

def low_pass_filter(data, threshold):
    mask = np.abs(data) < threshold
    return data * mask

def band_pass_filter(data, low_threshold, high_threshold):
    mask = (np.abs(data) > low_threshold) & (np.abs(data) < high_threshold)
    return data * mask

# Apply filters
threshold_high = 100
threshold_low = 20
psi_high_pass = apply_filter(psi_freq_shifted, lambda data: high_pass_filter(data, threshold_high))
psi_low_pass = apply_filter(psi_freq_shifted, lambda data: low_pass_filter(data, threshold_low))
psi_band_pass = apply_filter(psi_freq_shifted, lambda data: band_pass_filter(data, threshold_low, threshold_high))

# Perform inverse FFT to get filtered spatial data
psi_high_pass_spatial = ifftn(fftshift(psi_high_pass))
psi_low_pass_spatial = ifftn(fftshift(psi_low_pass))
psi_band_pass_spatial = ifftn(fftshift(psi_band_pass))

# Plotting the results
fig = plt.figure(figsize=(18, 12))

# Original Data
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, T, np.abs(psi), cmap='viridis')
ax1.set_title('Original Wave Function')
ax1.set_xlabel('Space (x)')
ax1.set_ylabel('Time (t)')
ax1.set_zlabel('Amplitude')

# High-Pass Filtered Data
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, T, np.abs(psi_high_pass_spatial), cmap='viridis')
ax2.set_title('High-Pass Filtered')
ax2.set_xlabel('Space (x)')
ax2.set_ylabel('Time (t)')
ax2.set_zlabel('Amplitude')

# Low-Pass Filtered Data
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, T, np.abs(psi_low_pass_spatial), cmap='viridis')
ax3.set_title('Low-Pass Filtered')
ax3.set_xlabel('Space (x)')
ax3.set_ylabel('Time (t)')
ax3.set_zlabel('Amplitude')

# Band-Pass Filtered Data
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, T, np.abs(psi_band_pass_spatial), cmap='viridis')
ax4.set_title('Band-Pass Filtered')
ax4.set_xlabel('Space (x)')
ax4.set_ylabel('Time (t)')
ax4.set_zlabel('Amplitude')

# Frequency Domain - High-Pass
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(KX, KT, np.abs(psi_high_pass), cmap='plasma')
ax5.set_title('High-Pass Filter (Frequency Domain)')
ax5.set_xlabel('Spatial Frequency (kx)')
ax5.set_ylabel('Temporal Frequency (kt)')
ax5.set_zlabel('Magnitude')

# Frequency Domain - Low-Pass
ax6 = fig.add_subplot(236, projection='3d')
ax6.plot_surface(KX, KT, np.abs(psi_low_pass), cmap='plasma')
ax6.set_title('Low-Pass Filter (Frequency Domain)')
ax6.set_xlabel('Spatial Frequency (kx)')
ax6.set_ylabel('Temporal Frequency (kt)')
ax6.set_zlabel('Magnitude')

plt.tight_layout()
plt.show()