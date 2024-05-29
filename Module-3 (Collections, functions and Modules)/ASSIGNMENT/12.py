#Write a Python program to convert a list of characters into a string

def list_to_string(char_list):
    return ''.join(char_list)

# Example:
characters = ['H', 'e', 'l', 'l', 'o']
result_string = list_to_string(characters)
print("List of characters:", characters)
print("Converted string:", result_string)
