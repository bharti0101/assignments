## Write python program that swap two number with temp variable and
#without temp variable.

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
print(f"numbers before first swap num1 : {num1}, num2 : {num2}")
#swap using temp
temp = num1
num1 = num2
num2 = temp
print(f"numbers after first swap num1 : {num1}, num2 : {num2}")

#swap without using temp
print(f"values before second swap num1 : {num1}, num2 : {num2}")
num1, num2 = num2, num1
print(f"values after second swap num1 : {num1}, num2 : {num2}")