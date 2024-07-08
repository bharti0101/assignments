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
