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

