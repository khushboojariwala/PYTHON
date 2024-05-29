#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

num_1 = int(input("Enter a number1 : "))
num_2 =int(input ("Enter a number2 : "))

if num_1 == num_2 or num_1 + num_2 == 5 or num_1 - num_2 == 5 :
    print("TRUE")

else:
    print("FALSE")