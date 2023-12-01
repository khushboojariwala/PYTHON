#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

# Creating a dictionary with keys as numbers between 1 and 15
my_dict = {num: f"value_{num}" for num in range(1, 16)}

print("Dictionary with keys from 1 to 15:", my_dict)
