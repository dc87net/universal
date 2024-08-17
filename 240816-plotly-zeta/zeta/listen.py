from sympy import isprime
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import simpleaudio as sa

# Binary strings
binary_strings = ['1011', '1001', '0000', '1101', '0000', '0100', '1110', '1111', '1100', '1011']

# Convert binary to decimal
decimal_values = [int(b, 2) for b in binary_strings]
print("Decimal values:", decimal_values)

# Convert binary to hexadecimal
hex_values = [hex(int(b, 2))[2:].upper() for b in binary_strings]
print("Hexadecimal values:", hex_values)

# Check if the decimal values are prime
prime_flags = [isprime(d) for d in decimal_values]
print("Prime flags:", prime_flags)

# Print decimal values with prime information
for d, p in zip(decimal_values, prime_flags):
    print(f"{d} is {'prime' if p else 'not prime'}")

# Plot the binary strings as a signal
plt.figure(figsize=(10, 4))
plt.stem(range(len(binary_strings)), decimal_values)
plt.title('Binary Sequence as Decimal Values')
plt.xlabel('Index')
plt.ylabel('Decimal Value')
plt.show()

# Convert binary strings to a PCM signal (simple approach)
pcm_signal = np.array(decimal_values, dtype=np.float32)
pcm_signal = (pcm_signal - np.min(pcm_signal)) / (np.max(pcm_signal) - np.min(pcm_signal))  # Normalize

# Loop the signal to play for approximately 10 seconds
sample_rate = 8000
duration = 10  # seconds
num_repeats = int((sample_rate * duration) / len(pcm_signal))
looped_pcm_signal = np.tile(pcm_signal, num_repeats)

# Fourier analysis of the signal
fourier_transform = np.fft.fft(looped_pcm_signal)
frequencies = np.fft.fftfreq(len(fourier_transform), d=1/sample_rate)

# Plot the Fourier transform (magnitude spectrum)
plt.figure(figsize=(10, 4))
plt.plot(frequencies, np.abs(fourier_transform))
plt.title('Fourier Transform of the Signal')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.show()

# Write the looped PCM signal to a WAV file (normalized to 16-bit PCM)
looped_pcm_signal_int16 = np.int16(looped_pcm_signal * 32767)  # Convert to 16-bit PCM
write("binary_signal_looped.wav", sample_rate, looped_pcm_signal_int16)

# Load the saved WAV file using pydub for playback
audio = AudioSegment.from_wav("binary_signal_looped.wav")

# Play the audio using simpleaudio
play_obj = sa.play_buffer(audio.raw_data, num_channels=1, bytes_per_sample=2, sample_rate=sample_rate)
play_obj.wait_done()

print("Playing the looped signal as audio...")
print("Sound saved as 'binary_signal_looped.wav'")
