#  Write a python program to sum of the first n positive integers.

n = int(input("enter the range: "))
s = 0
for i in range(1, n + 1):
    s = s + i
    if i == n - 1:
        print(f"the sum of first n number is: {s}")
        break
