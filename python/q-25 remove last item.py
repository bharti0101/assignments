# How will you remove last object from a list?
#Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
list1 = [2,33,222,14,25]
#-->list1[-1]=25

#-> using slicing
print(list1[:-1])

#-> using list comprehension
print([i for i in list1[:-1]])

#-> using pop function
list1 = [2,33,222,14,25]
l = list1.pop()
print(list1)

#-> using del keyword
list1 = [2,33,222,14,25]
del list1[-1]
print(list1)

#-> using remove method
list1 = [2,33,222,14,25]
list1.remove(25)
print(list1)

#pop, remove, del make changes to the original list
#pop can also remove the ele at specific index provided the index value
#pop returns the popped ele while delete does not return anything unless explicity printed out
#remove removes the ele by its value not by its index
#another method clear() removes all the items from the list




