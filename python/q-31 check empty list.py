#  Write a Python program to check a list is empty or not.

#method - 1
def checkEmpty(lis):
        if lis:
            return "list not empty"
        else:
            return "list empty"

li = input("enter the list elements: ").split()
result = checkEmpty(li)
print(result)

#method - 2
def ifEmpty(lis):
    if len(lis)== 0:
        return "list empty"
    else:
        return "list contain elements"

list1 = input("enter the list elements: ").split()
print(ifEmpty(list1))

#method - 3 (using numpy)

def checkEle(li):
    import numpy as np
    arr = np.array(li)
    if arr.size != 0:
        return "not empty"
    else:
        return "empty"

list2 = input("enter the list elements: ").split()
print(checkEle(list2))


