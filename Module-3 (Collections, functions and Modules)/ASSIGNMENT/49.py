#Write a Python function to check whether a number is in a given range

def in_range(num, start, end):
    return start <= num <= end

# Define the range
start_range = 10
end_range = 20

# Number to check
number_to_check = 15  

# Print the result
result = in_range(number_to_check, start_range, end_range)
print(f"The number {number_to_check} is in the range {start_range} to {end_range}: {result}")
