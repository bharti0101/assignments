#  Write a Python program to count occurrences of a substring in a string.

#method - 1
str_inp = input("enter the string: ")
sub_str = input("enter the substring: ")
count = 0
for i in range(len(str_inp) - len(sub_str) + 1):
    if str_inp[i:i + len(sub_str)] == sub_str:
        count += 1
print(count)

#method - 2
str_inp = input("enter the string: ")
sub_str = input("enter the substring: ")
freq = str_inp.count(sub_str)
print(freq)