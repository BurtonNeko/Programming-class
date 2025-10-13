# Frequency analysis is a method of breaking certain ciphers which involves counting the frequency of letters/symbols
# because English has quite a clear distribution of letters, with spikes on common letters such as 'e', 'i' and 's'

# Ask the user for a filename
# open and read the file 
# and count how many instances of each letter are in the program
# hint: use a dictionary!

# Additional hints:
# - Remember to handle the case where the file might not exist
# - You'll need to check each character to see if it's a letter
# - Dictionary pattern: if key exists, increment; if not, set to 1
# - Consider converting to lowercase for consistent counting
import string

filename = input('Enter the filename: ')

letter_counts = {}

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

        for char in content.lower():
            if char in string.ascii_lowercase:  
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1

    for letter in sorted(letter_counts):
        print(f'{letter}: {letter_counts[letter]}')

except FileNotFoundError:
    print('File not found. Please check the filename and try again.')
