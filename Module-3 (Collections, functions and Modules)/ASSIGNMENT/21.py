#Write a Python program to convert a tuple to a string.

def tuple_to_string(input_tuple):
    return ''.join(map(str, input_tuple))

# Example:
my_tuple = (1, 2, 3, 4, 5)
result_string = tuple_to_string(my_tuple)
print("Tuple:", my_tuple)
print("Converted string:", result_string)
