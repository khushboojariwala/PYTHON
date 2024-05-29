#Write a Python program to count the number of characters (character frequency) in a string

string_1 = input("Enter a string: ")

char_frequency = {}

for char in string_1:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

for char, count in char_frequency.items():
    print(f"'{char}': {count} times")
