#  Write a Python program to count the occurrences of each word in a given sentence
#method - 1
sen = input("enter the sentence: ").split()
dict={}
for i in sen:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#method - 2
sentence = input()
word = sentence.split()
freq={}
for i in word:
    freq[i] = sentence.count(i)
for i, j in freq.items():
    print(f"{i}:{j}")

