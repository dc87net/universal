import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
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

# Plot the results of Fourier Transform
plt.figure(figsize=(12, 6))

# Plot magnitude of FFT of the original Zeta function
plt.subplot(221)
plt.plot(np.abs(zeta_fft))
plt.title('Magnitude of FFT of Riemann Zeta Function')

# Plot phase of FFT of the original Zeta function
plt.subplot(222)
plt.plot(np.angle(zeta_fft))
plt.title('Phase of FFT of Riemann Zeta Function')

# Plot magnitude of FFT of the convolved signal
plt.subplot(223)
plt.plot(np.abs(convolved_fft))
plt.title('Magnitude of FFT of Convolved Signal')

# Plot phase of FFT of the convolved signal
plt.subplot(224)
plt.plot(np.angle(convolved_fft))
plt.title('Phase of FFT of Convolved Signal')

plt.tight_layout()
plt.show()