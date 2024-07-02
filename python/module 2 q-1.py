# Write a Python program to check if a number is positive, negative or zero.

num = int(input('enter the no: '))
if num < 0:
    print("the no is negative")
elif num > 0:
    print("the no is positive")
elif num == 0:
    print("no is zero")
else:
    print("enter the valid integer")