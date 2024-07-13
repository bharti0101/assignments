#  Write a Python function that takes two lists and returns true if they have
# at least one common member.

lis1 = input("enter the elements separated by an space: ").split()
lis2 = input("enter the elements separated by an space: ").split()

#method 1 - naive method using loops

def CompareList(list1, list2):
    res = False
    for i in list1:
        for j in list2:
            if i == j:
                res = True
    return res

print(CompareList(lis1, lis2))

#method 2 - using set property , & (which returns True for intersection element/s present in set otherwise False)

lis1 = input("enter the elements for the first list separated by a space: ")
lis2 = input("enter the elements for the second list separated by a space: ")
def CompList(listt1,listt2):
    set1 = set(listt1)
    set2 = set(listt2)
    if set1 & set2:
        return True
    else:
        return False

print(CompList(lis1,lis2))

#method 3 - using set inbuilt function set.intersection

liss1 = input("enter the list's element separated by space: ").split()
liss2 = input("enter the list's element separated by space: ").split()

def ListComparision(listtt1, listtt2):
    sett1 = set(liss1)
    sett2 = set(liss2)
    if sett1.intersection(sett2):
        return True
    else:
        return False
print(ListComparision(liss1, liss2))
