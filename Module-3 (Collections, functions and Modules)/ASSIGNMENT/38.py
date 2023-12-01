#Write a Python program to check multiple keys exists in a dictionary

def check_keys(dictionary, keys_to_check):
    return all(key in dictionary for key in keys_to_check)

# Example:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'b', 'd']

if check_keys(my_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
