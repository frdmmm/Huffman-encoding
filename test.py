import string
import random

# Generate a list of characters reachable by keyboard and shift key
keyboard_characters = list(string.ascii_letters + string.digits + string.punctuation + ' ')

# Shuffle the list to simulate a random order of appearance
random.shuffle(keyboard_characters)

# Create a dictionary with each character appearing once
original_frequency_dict = {char: 1 for char in keyboard_characters}

# Define English letter frequencies (based on approximate frequencies in English text)
english_letter_frequencies = {
    'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
    'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
    'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
    'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.49,
    'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10,
    'z': 0.07
}

# Modify character frequencies according to English letter frequencies
modified_frequency_dict = original_frequency_dict.copy()
for char in modified_frequency_dict:
    if char.isalpha():
        modified_frequency_dict[char] = int(original_frequency_dict[char] * (english_letter_frequencies[char.lower()] / 100))
    # For non-alphabetic characters, use a generic frequency
    else:
        modified_frequency_dict[char] = int(original_frequency_dict[char] * 2)

# Print the modified frequencies
print(modified_frequency_dict)
