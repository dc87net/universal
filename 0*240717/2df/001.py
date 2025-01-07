
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/Users/douglas/Downloads/solid_blue.ppm'
image = Image.open(image_path).convert('L')  # Convert to grayscale
image_array = np.array(image)

# Compute the 2D Fourier transform
f_transform = np.fft.fft2(image_array)
f_shifted = np.fft.fftshift(f_transform)

# Compute the magnitude spectrum
magnitude_spectrum = 20*np.log(np.abs(f_shifted))

# Plot the magnitude spectrum
plt.figure(figsize=(20, 20))
plt.imshow(magnitude_spectrum, cmap='jet')
plt.title(f'2D FT of {image_path}')
plt.axis('off')  # Hide the axes
plt.show()

#
# if line 15 is edited as follows, adding +1 offset, we get the correct answer (attached):
# `magnitude_spectrum = 20*np.log(np.abs(f_shifted+1))`
