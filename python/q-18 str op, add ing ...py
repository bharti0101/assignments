#  Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.

inp_str = input("enter the string: ")
if len(inp_str)<3:
    print(f"unchanged string: {inp_str}")
elif len(inp_str)>=3:
    if inp_str[-3:]=='ing':
        print(f"added -ly to the input string {inp_str} making it : {inp_str+'ly'}")
    else:
        print(f"added -ing at the end of the {inp_str} making it : {inp_str+'ing'} ")

