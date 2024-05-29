#Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a letter: ")

letter = letter.lower()   #Convert the letter to lowercase

vowels = {'a', 'e', 'i', 'o', 'u'}


if letter in vowels:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")