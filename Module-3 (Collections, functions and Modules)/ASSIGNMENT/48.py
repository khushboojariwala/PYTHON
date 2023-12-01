#Write a Python function to calculate the factorial of a number (anonnegative integer)

n=int(input("enter the number:"))

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
result=factorial(n)
print(f"the factorial of {n} is:{result}")