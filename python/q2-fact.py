#  Write a Python program to get the Factorial number of given number.

num = int(input("enter the number: "))
fact = num - 1
while fact > 0:
    num=num*fact
    fact = fact - 1
print(f"factorial is: {num}")
