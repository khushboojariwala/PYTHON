#Write a Python program to find the second smallest number in a list

def second_smallest_number(input_list):
    unique_sorted = sorted(set(input_list))
    if len(unique_sorted) > 1:
        return unique_sorted[1]
    else:
        return "List doesn't have a second smallest element"

# Example:
my_list = [3, 1, 4, 5, 2, 6, 7]
second_min = second_smallest_number(my_list)
print("Original List:", my_list)
print("Second smallest number:", second_min)
