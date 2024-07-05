# Write a Python function to reverse a string if its length is a multiple of 4.

str1 = input("enter the string: ")
def reverse_str(string):
    if len(string)%4==0:
      str2=string[-1::-1]
      return(str2)
    else:
        return"The length of the string is not a multiple of 4."

res=reverse_str(str1)
print(res)

