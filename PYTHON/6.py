#Write python program that swap two number with temp variable and without temp variable:-

#Swap with a Temporary Variable:

a=10
b=20

print("before swapping value:")
print("a=",a)
print("b=",b)

temp=a
a=b
b=temp

print("After Swapping Value:")
print("a=",a)
print("b=",b)

#Swap Without a Temporary Variable

a=30
b=40

print("before swapping value:")
print("a=",a)
print("b=",b)

a=a+b
b=a-b
a=a-b

print("After Swapping Value:")
print("a=",a)
print("b=",b)