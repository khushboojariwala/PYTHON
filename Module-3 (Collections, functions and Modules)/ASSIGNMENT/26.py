#Write a Python program to replace last value of tuples in a list.

tuple1= [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 100

modified_tuples = [t[:-1] + (new_value,) for t in tuple1]

print("Original Tuples:",tuple1)
print("Tuples with Last Value Replaced:", modified_tuples)
