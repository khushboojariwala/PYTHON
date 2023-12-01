#Write a Python program to remove an empty tuple(s) from a list of tuples

list_of_tuples = [(1, 2), (), (3, 4), (), (), (5,), (), (6, 7, 8), ()]

# Remove empty tuples:
filtered_tuples = list(filter(lambda x: len(x) != 0, list_of_tuples))

print("Original List of Tuples:", list_of_tuples)
print("List of Tuples after Removing Empty Tuples:", filtered_tuples)
