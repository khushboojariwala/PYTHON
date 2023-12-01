#Write a Python program to check whether a list contains a sub list

def is_sublist(main_list, sub_list):
    if len(sub_list) == 0:
        return True
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i + len(sub_list)] == sub_list:
            return True
    return False

# Example:
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
sublist1 = [3, 4, 5]
sublist2 = [8, 9]

print(is_sublist(list1, sublist1))  # Output: True
print(is_sublist(list1, sublist2))  # Output: False
