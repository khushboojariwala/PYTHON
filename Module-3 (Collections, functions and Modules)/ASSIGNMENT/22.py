#Write a Python program to check whether an element exists within a tuple.

def check_element_in_tuple(input_tuple, element):
    return element in input_tuple

# Example:
my_tuple = (11, 22, 33, 44, 55)
element_to_check = 33

if check_element_in_tuple(my_tuple, element_to_check):
    print(f"{element_to_check} exists in the tuple")
else:
    print(f"{element_to_check} does not exist in the tuple")
