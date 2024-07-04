# Write a Python program to find the first appearance of the substring
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
#whole 'not'...'poor' substring  with 'good'. Return the resulting string.

str1 = input("enter thr string: ")
not_index = str1.find('not')
print(f"first appearance of 'not' : {not_index}")
poor_index = str1.find('poor')
print(f"first appearance of 'poor' : {poor_index}")
if not_index < poor_index:
    nt_poor_index = not_index
    print(f"first appearance of 'not.....poor' : {nt_poor_index}")
    print(f"the resulting string after replacement : {str1.replace(str1[str1.find('not'):str1.find('poor')+4],'good')}")