#  Write a Python program to remove duplicates from a list.
#method - 1 (input must be int, use set)
ls =input("enter the elements of the list separated by a space: ").split()
ls2=[]
for i in ls:
    ls2.append(int(i))
print(ls2)
st = set(ls2)
print(list(st))
#method-2(any dtype input, use 'not in')
inp_list = input("enter the list elements separated by a space: ").split(" ")
listt = []
for ele in inp_list:
    if ele not in listt:
        listt.append(ele)
print(listt)

#method-3(using numpy, inp must be int)

def uniqueelements(lst):
    import numpy as np
    #converting list into numpy array
    np_array = np.array(lst)
    #using np.unique() fn from np library to display unique elements
    unique_arr = np.unique(np_array)
    #using method from numpy array object to convert the numpy array back to the list
    arrtolist = unique_arr.tolist()
    return arrtolist
input_lst = input("enter the numbers separated by an space: ").split()
print(uniqueelements(input_lst))


