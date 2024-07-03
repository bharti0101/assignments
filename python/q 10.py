#  Write a Python program that will return true if the two given integer values are equal or their sum or difference
# is 5.

a = int(input("enter the num 1: "))
b = int(input("enter the num 2: "))


def check_no(i, j):
    if i == j or abs(i - j) == 5 or i + j == 5:
        return True
    else:
        return False


print(check_no(a, b))
