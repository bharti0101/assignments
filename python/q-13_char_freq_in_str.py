#  Write a Python program to count the number of characters (character frequency) in a string

#method - 1
str = input("enter the string: ")
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)