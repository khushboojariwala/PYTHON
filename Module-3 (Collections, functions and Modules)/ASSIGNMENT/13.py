#Write a Python program to select an item randomly from a list.

import random

def select_random_item(list1):
    return random.choice(list1)

# Example:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_item = select_random_item(my_list)
print("Randomly selected item:", random_item)
