#Write a Python program to map two lists into a dictionary

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Mapping two lists into a dictionary
mapped_dict = dict(zip(keys, values))

print("Mapped Dictionary:", mapped_dict)
