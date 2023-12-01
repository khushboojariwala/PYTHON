#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

def generate_square_list(start, end):
    squares = [i ** 2 for i in range(start, end + 1)]
    return squares

# Generate squares of numbers between 1 and 30
squared_values = generate_square_list(1, 30)

# Print the first and last 5 elements
first_5 = squared_values[:5]
last_5 = squared_values[-5:]

print("First 5 elements:", first_5)
print("Last 5 elements:", last_5)
