# Write a Python program to get the Factorial number of given number.

number = (input("enter a number:"))
number_ = int(number)

if number_ < 0:
    print("Please enter the valid number.")
elif number_ == 0:
    print("Factorial of 0 is 1")
else:
    factorial=1
    
    for i in range (1,number_+1):
        factorial = factorial * i
        
    print(f"The Factorial Of {number_} Is {factorial}")