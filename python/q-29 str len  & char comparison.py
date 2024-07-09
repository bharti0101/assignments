#  Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.

def countMatchingString(list_string):
    n=0
    for string in list_string:
        string = string.strip()
        if len(string) >= 2 and string[0]==string[-1]:
            n += 1
    return n
ls_string = input("enter the strings separated by a comma: ").split(",")
print(countMatchingString(ls_string))
