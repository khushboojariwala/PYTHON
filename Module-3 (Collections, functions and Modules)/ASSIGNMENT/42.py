#Write a Python program to print all unique values in a dictionary.

my_dict = {'a': 100, 'b': 200, 'c': 400, 'd': 300, 'e': 200}
unique_values = set(my_dict.values())

print("Dictionary:", my_dict)
print("Unique Values:", unique_values)
