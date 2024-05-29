#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

string_1 = input("Enter a string: ")

if len(string_1) >= 3:
    if string_1[-3:] == "ing":
        result = string_1 + "ly"
    else:
        result = string_1 + "ing"
else:
    result = string_1

print("Result: ",result)