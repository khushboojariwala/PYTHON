#Write a Python program to check a list is empty or not.

def list_empty(list1):
    return len(list1) == 0

# Example:
empty_list = []
if list_empty(empty_list):
    print("The list is empty")
else:
    print("The list is not empty")

non_empty_list = [1, 2, 3]

if list_empty(non_empty_list):
    print("The list is empty")
else:
    print("The list is not empty")
