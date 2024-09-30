# Write a Python program to get unique values from a list

li = [23, 29, 1, 8, 34, 28, 23, 1, 89, 29]
uni_val = list(set(li))
print(uni_val)

#using dictionary

li = [23, 29, 1, 8, 34, 28, 23, 1, 89, 29]
di = {}
uni_li = []
for i in li:
    if i not in di:
        di[i]=1
    else:
        continue
print(list(di.keys()))



