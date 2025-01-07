# Define the mapping for angular position (theta), radius (r), and height (z)
def frequency_to_cylindrical(f, base=440):
    import numpy as np
    octave = int(np.log2(f / base))  # Determine the octave number relative to base frequency
    note_index = int(12 * np.log2(f / (base * 2**octave)))  # Determine the note within the octave
    theta = 2 * np.pi * note_index / 12  # Angular position
    z = octave  # Height corresponds to the octave number
    r = np.log(f / base)  # Logarithmic radius
    return r, theta, z

def cylindrical_to_frequency(r, theta, z, base=440):
    import numpy as np
    return base * np.exp(r)

# Frequencies for the melody (Twinkle, Twinkle Little Star)
base_frequency = 440  # A4
notes = [0, 0, 7, 7, 9, 9, 7,  # "Twinkle, Twinkle, Little Star"
         5, 5, 4, 4, 2, 2, 0,  # "How I Wonder What You Are"
         7, 7, 5, 5, 4, 4, 2,  # "Up Above the World So High"
         7, 7, 5, 5, 4, 4, 2,  # "Like a Diamond in the Sky"
         0, 0, 7, 7, 9, 9, 7,  # "Twinkle, Twinkle, Little Star"
         5, 5, 4, 4, 2, 2, 0]  # "How I Wonder What You Are"

# Calculate frequencies using equal temperament formula
frequencies_song = [base_frequency * (2 ** (n / 12)) for n in notes]

# Map frequencies to cylindrical coordinates
cylindrical_coords = [frequency_to_cylindrical(f) for f in frequencies_song]

# Recover frequencies from cylindrical coordinates
recovered_frequencies = [cylindrical_to_frequency(r, theta, z) for r, theta, z in cylindrical_coords]

# Map notes to their names in C major scale
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
named_notes = [note_names[n % 12] for n in notes]

# Create a DataFrame for comparison
import pandas as pd
df_cylindrical_mapping = pd.DataFrame({
    "Note": named_notes,
    "Original Frequency (Hz)": frequencies_song,
    "Radius (r)": [r for r, theta, z in cylindrical_coords],
    "Theta (rad)": [theta for r, theta, z in cylindrical_coords],
    "Height (z)": [z for r, theta, z in cylindrical_coords],
    "Recovered Frequency (Hz)": recovered_frequencies
})

# Save the DataFrame to a CSV file for local inspection
df_cylindrical_mapping.to_csv("cylindrical_frequency_mapping.csv", index=False)

# Print the DataFrame for quick review
print(df_cylindrical_mapping)
