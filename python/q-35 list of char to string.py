#Write a Python program to convert a list of characters into a string.

#method - 1 --> using for loop
li = ['l','i','s','t']
li2=['p','r','i','y','a','l',4,0,2,3.8,8.6]
def ListCharToString(list1):
    ch = ''
    for i in list1:
        ch = ch + i
    return ch
print(ListCharToString(li))

#method-2 --> using string join function

st = "".join(li)
print(st)

#method-3 --> using map function when few elements are non string as well like int, float
m = map(str,li2)
s=''.join(m)
print(s)

#method-4 --> using generator expression similar to list comprehension
string1 = "".join(str(i) for i in li2)
print(string1)
