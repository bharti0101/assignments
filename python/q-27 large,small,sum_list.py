#  Write a Python function to get the largest number, smallest num and sum
# of all from a list.

# method - 1

def largest(listofnum):
    maxi = listofnum[0]  # suppose
    for i in listofnum:
        if maxi < i:
            maxi = i
    return maxi


def smallest(listofnum):
    mini = listofnum[0]  # suppose
    for i in listofnum:
        if mini > i:
            mini = i
    return mini


def sumofelements(listofnum):
    elesum = 0  # let
    for i in listofnum:
        elesum += i
    return elesum


li = [2, 5, 0, 6, 1, 4, 3]
maximum = largest(li)
print(maximum)
minimum = smallest(li)
print(minimum)
addition = sumofelements(li)
print(addition)

#method - 2

lis = [2, 5, 0, 6, 1, 4, 3]
def findmin(listele):
    return min(listele)
def findmax(listele):
    return max(listele)
def findsum(listele):
    return sum(listele)
print(findmin(lis))
print(findmax(lis))
print(findsum(lis))

#method - 3

n = int(input("enter the no of elements to be inserted: "))
lis = []
print("enter the elements: ")
for i in range(0,n):
    ele = int(input())
    lis.append(ele)
lis.sort()
print(lis)
def findminimum(sortedlist):
    return sortedlist[0]
def findmaximum(sortedlist):
    return sortedlist[-1]
def findsum(sortedlist):
    return sum(sortedlist)
print(findminimum(lis))
print(findmaximum(lis))
print(findsum(lis))

#method - 4

li = input("enter the elements: ").split()
li2=[]
for i in li:
    li2.append(int(i))

li2.sort()
print(f"the min value is: {li2[0]}, the max value is: {li2[-1]}, the sum of the elements is: {sum(li2)}")