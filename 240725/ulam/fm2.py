import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import spectrogram, find_peaks
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

# Plot the original Zeta function
plt.figure(figsize=(10, 4))
plt.plot(x, zeta_values)
plt.title('Riemann Zeta Function')
plt.xlabel('x')
plt.ylabel('zeta(x)')
plt.show()

# Plot the impulse response
plt.figure(figsize=(10, 4))
plt.stem(np.arange(len(h)), h)
plt.title('Impulse Response (Derived from Prime Numbers)')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.show()

# Plot the convolved signal
plt.figure(figsize=(10, 4))
plt.plot(np.real(convolved_signal))
plt.title('Convolved Signal')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.show()

# Focus on the segment showing FM characteristics
zoom_segment = np.real(convolved_signal[:200])

# Plot the zoomed segment of the convolved signal
plt.figure(figsize=(10, 4))
plt.plot(zoom_segment)
plt.title('Zoomed Segment of Convolved Signal')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.show()

# Frequency analysis using STFT
f, t, Sxx = spectrogram(zoom_segment, fs=1.0, nperseg=20, noverlap=10, nfft=128)

# Plot the spectrogram
plt.figure(figsize=(10, 6))
plt.pcolormesh(t, f, np.abs(Sxx), shading='gouraud')
plt.title('Spectrogram of Zoomed Segment')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar(label='Intensity')
plt.show()

# Detailed frequency analysis
fft_zoom = fft(zoom_segment)
freqs = np.fft.fftfreq(len(fft_zoom))

# Find peaks in the frequency domain
peaks, _ = find_peaks(np.abs(fft_zoom), height=10)

# Plot the detailed frequency analysis
plt.figure(figsize=(10, 4))
plt.plot(freqs, np.abs(fft_zoom))
plt.plot(freqs[peaks], np.abs(fft_zoom)[peaks], "x")
plt.title('Detailed Frequency Analysis of Zoomed Segment')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()