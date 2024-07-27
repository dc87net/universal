import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import hilbert, find_peaks
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

# Perform Hilbert Transform to get the analytic signal
analytic_signal = hilbert(zoom_segment)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = np.diff(instantaneous_phase)

# Identify the carrier frequency (dominant frequency)
fft_zoom = fft(zoom_segment)
freqs = np.fft.fftfreq(len(fft_zoom))
dominant_frequency_index = np.argmax(np.abs(fft_zoom))
carrier_frequency = freqs[dominant_frequency_index]

# Estimate phase sensitivity k_p
modulating_signal = instantaneous_phase - carrier_frequency * np.arange(len(instantaneous_phase))

# Plot the results
plt.figure(figsize=(10, 4))
plt.plot(instantaneous_phase)
plt.title('Instantaneous Phase of the Zoomed Segment')
plt.xlabel('Time')
plt.ylabel('Phase (radians)')
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(instantaneous_frequency)
plt.title('Instantaneous Frequency of the Zoomed Segment')
plt.xlabel('Time')
plt.ylabel('Frequency (radians/sample)')
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(modulating_signal)
plt.title('Estimated Modulating Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# Print the estimated carrier frequency and phase sensitivity
print(f"Estimated Carrier Frequency: {carrier_frequency}")
print(f"Estimated Phase Sensitivity (k_p): {np.std(modulating_signal)}")