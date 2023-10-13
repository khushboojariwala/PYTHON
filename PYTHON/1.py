#Write a Python program to check if a number is positive, negative or zero.
       
number = (input("enter a number:"))
number_ =float(number)

if number_ > 0 :
    print("The Number Is Positive")
elif number_ < 0 :
    print("The Number Is Negative")
else :
    print("The Number Is Zero")