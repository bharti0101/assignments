# Write a Python program to get the Fibonacci series of given range.


#1 1 2 3 5 8 13 21......
#taking n as first n numbers of the series
n = int(input('enter the range '))
print(f"the fibonacci series for the range {n} are as : ")
n1 = 1
print(n1)
n2 = 1
print(n2)
#range - (0,n-2) as n1 and n2 already printed
for i in range(0 , n-2):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
