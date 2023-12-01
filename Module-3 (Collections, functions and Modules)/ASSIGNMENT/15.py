#Write a Python program to get unique values from a list

def get_unique_value(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example:
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_values_ordered = get_unique_value(original_list)
print("Original List:", original_list)
print("Unique Values (Preserving Order):", unique_values_ordered)
