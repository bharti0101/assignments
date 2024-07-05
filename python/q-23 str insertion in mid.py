#  Write a Python function to insert a string in the middle of a string.

def insertString(txt1, txt2):
    txt_len = len(txt1)
    pos = txt_len//2
    new_txt = txt1[:pos]+txt2+txt1[pos:]
    return new_txt

text1 = input("enter the string: ")
text2 = input("enter the text to be inserted: ")
res = insertString(text1,text2)
print(res)
