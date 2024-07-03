# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
num3 = int(input("enter the num3: "))
if num1==num2 or num1==num3 or num2==num3 :
    sum = 0
    print(f"the sum is {sum}")

else :
    sum = num1 + num2 + num3
    print(f"the sum is {sum}")