#4.Write a Python function to get the largest number, smallest num and sum of all from a list.

def get_list(nums):
    if not nums:
        return None, None, 0
    
    largest = max(nums)
    smallest = min(nums)
    total_sum = sum(nums)
    
    return largest, smallest, total_sum

numbers = [17, 45, 29, 67, 7, 89]
largest_num, smallest_num, sum_all = get_list(numbers)

print(f"Largest number: {largest_num}")
print(f"Smallest number: {smallest_num}")
print(f"Sum of all numbers: {sum_all}")
