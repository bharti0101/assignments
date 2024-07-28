#  Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

#method - 1 --> using for loop

li = [13, 6, 13, 30, 12, 3, 3, 'july', 'august', 'july', 3.0, 's', 3.0]

def unique(list1):
    res=[]
    for i in list1:
        if i not in res:
            res.append(i)
    return res
print(unique(li))

#method-2 --> using set property

def unique2(list2):
    set1 = set(list2)
    res_list = list(set1)
    return res_list

print(unique2(li))

#method-3 --> using numpy.unique

import numpy as np
def unique3(list3):
    arr = np.array(list3)
    ret_lis = np.unique(arr)
    return ret_lis
print(list(unique3(li)))