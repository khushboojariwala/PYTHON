main_string = input("Enter the main string: ")
string_to_insert = input("Enter the string to insert: ")

middle_index = len(main_string) // 2
result = main_string[:middle_index] + string_to_insert + main_string[middle_index:]

print("Result:", result)
