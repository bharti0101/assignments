#  Write a Python program to get a single string from two given strings, separated by a space and swap the first two
# characters of each string.

str1 = input("enter first string: ")
str2 = input("enter second string: ")
#inp
#str1 = abc, str2 = xyz, str = abc xyz --> xyc abz
new_s1 = str2[0:2] + str1[2:]
new_s2 = str1[0:2] + str2[2:]
fin = new_s1 + ' ' + new_s2
print(fin)
