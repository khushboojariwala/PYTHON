#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

string_1 = input("Enter a string: ")

index_not = string_1.find('not')
index_poor = string_1.find('poor')

if index_not != -1 and index_poor != -1 and index_not < index_poor:
    result = string_1[:index_not] + 'good' + string_1[index_poor + 4:]
else:
    result = string_1

print("Result: " + result)