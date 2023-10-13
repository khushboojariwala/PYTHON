#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num_1 = int(input("Enter a number1 : "))
num_2 = int(input("Enter a number2 : "))
num_3 = int(input("Enter a number3 : "))

if (num_1 == num_2) or (num_2 == num_3) or (num_3 == num_1) :
    print("sum is zero")

else:
    sum = num_1+num_2+num_3
    print (f"The ans of sum is {sum}")