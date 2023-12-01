#Write a Python script to sort (ascending and descending) a dictionary by value.

import operator

my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# Sorting dictionary by values in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))

print("Original Dictionary:", my_dict)
print("Dictionary Sorted by Values (Ascending):", sorted_dict_asc)


# Sorting dictionary by values in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))


print("Dictionary Sorted by Values (Descending):", sorted_dict_desc)
