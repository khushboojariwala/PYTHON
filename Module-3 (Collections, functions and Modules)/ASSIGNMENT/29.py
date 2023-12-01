#Write a Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

unzipped_lists = [[] for _ in range(len(list_of_tuples[0]))]

for tup in list_of_tuples:
    for i, item in enumerate(tup):
        unzipped_lists[i].append(item)

print("List of Tuples:", list_of_tuples)
print("Unzipped Lists:", unzipped_lists)
