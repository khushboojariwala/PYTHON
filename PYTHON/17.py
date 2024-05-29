#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) >= 2 and len(string2) >= 2:
    new_string = string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]
    print("Result:", new_string)
else:
    print("Both strings should have at least 2 characters for swapping.")
