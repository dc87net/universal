import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import hilbert
from mpmath import zeta

# Define the Riemann Zeta function over a complex plane
def zeta_function(x):
    return np.array([zeta(complex(xi, 0)).real for xi in x])

# Define an impulse response derived from prime numbers
def impulse_response(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    response = np.zeros(n)
    for p in primes:
        if p < n:
            response[p] = 1
    return response

# Ensure we sample the function with more than twice the highest frequency component
x = np.linspace(0.01, 50, 2000)  # Sufficient sampling rate to satisfy Nyquist-Shannon theorem
zeta_values = zeta_function(x)

# Define the impulse response
n = len(zeta_values)
h = impulse_response(n)

# Perform the convolution in the frequency domain
zeta_fft = fft(zeta_values)
h_fft = fft(h)
convolved_fft = zeta_fft * h_fft
convolved_signal = ifft(convolved_fft)

# Focus on the segment showing FM characteristics
zoom_segment = np.real(convolved_signal[:200])

# Sampling
sampling_rate = 20  # Samples per second
samples = zoom_segment[::sampling_rate]

# Quantization
num_levels = 16  # Number of quantization levels
min_val = np.min(samples)
max_val = np.max(samples)
quantized_levels = np.linspace(min_val, max_val, num_levels)
quantized_signal = np.digitize(samples, quantized_levels) - 1
quantized_signal_values = quantized_levels[quantized_signal]

# Encoding (For simplicity, we'll represent the quantized levels as binary codes)
encoded_signal = [format(level, '04b') for level in quantized_signal]

# Plot the original and quantized signals
plt.figure(figsize=(10, 4))
plt.plot(zoom_segment, label='Original Signal')
plt.plot(np.arange(0, len(zoom_segment), sampling_rate), quantized_signal_values, 'o', label='Quantized Signal')
plt.title('Original and Quantized Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Print the encoded signal
print("Encoded Signal:")
print(encoded_signal)