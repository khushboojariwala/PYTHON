#Write a Python program to create a dictionary from a string.
input_string = 'w3resource'

letter_count = {}
for letter in input_string:
    if letter.isalpha():           # Checking if the character is a letter
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

print(letter_count)

