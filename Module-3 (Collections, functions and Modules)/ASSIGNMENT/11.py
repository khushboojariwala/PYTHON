#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def get_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example:
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements_ordered = get_unique_elements(original_list)
print("Original List:", original_list)
print("List with Unique Elements:", unique_elements_ordered)
