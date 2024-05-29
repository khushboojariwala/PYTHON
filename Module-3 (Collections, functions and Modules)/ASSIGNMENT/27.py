#Write a Python program to find the repeated items of a tuple

my_tuple = (1, 2, 2, 3, 4, 4, 5, 5, 5)

# Using a set to store repeated items
repeated_items = set()
unique_items = set()

for item in my_tuple:
    if item in unique_items:
        repeated_items.add(item)
    else:
        unique_items.add(item)

print("Original Tuple:", my_tuple)
print("Repeated Items:", list(repeated_items))
