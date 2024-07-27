from sympy import isprime
import matplotlib.pyplot as plt

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
    plt.stem(range(len(binary_strings)), decimal_values, use_line_collection=True)
    plt.title('Binary Sequence as Decimal Values')
    plt.xlabel('Index')
    plt.ylabel('Decimal Value')
    plt.show()

# Plot the binary strings as a signal
plt.figure(figsize=(10, 4))
plt.stem(range(len(binary_strings)), decimal_values, use_line_collection=True)
plt.title('Binary Sequence as Decimal Values')
plt.xlabel('Index')
plt.ylabel('Decimal Value')
plt.show()

import sounddevice as sd

# Convert binary strings to a PCM signal (simple approach)
pcm_signal = np.array(decimal_values, dtype=np.float32)
pcm_signal = (pcm_signal - np.min(pcm_signal)) / (np.max(pcm_signal) - np.min(pcm_signal))  # Normalize

# Play the signal as sound
sd.play(pcm_signal, samplerate=8000)
sd.wait()

print("Playing the signal as audio...")