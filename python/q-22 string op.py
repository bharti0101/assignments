#  Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

str1 = input("enter the string: ")

def modified_string(string):
    if len(string)<2:
        new_str = string
    else:
        first_two = string[0:2]
        last_two = string[-2:]
        new_str = first_two+last_two
    return new_str

print(modified_string(str1))

