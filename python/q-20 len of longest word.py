# Write a Python function that takes a list of words and returns the length
#of the longest one.

lst = input("enter words separated by a space: ").split()
longest = 0
for words in lst:
    w_len = len(words)
    if w_len>longest:
        longest = w_len
print(f"length of the longest string is : {longest}")