#  Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.

#method - 1 using list comprehension + slicing
listt = [x**2 for x in range(1,31)]
print(listt[0: 5] + listt[-5:])

#method - 2 using for loop
liss = []
for i in range(1,31):
    liss.append(i**2)
print(liss[:5] + liss[-5:])