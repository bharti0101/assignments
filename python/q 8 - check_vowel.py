# Write a Python program to test whether a passed letter is a vowel or not.

vowel = ['a', 'e', 'i', 'o', 'u']
character = input("enter the character to be checked: ").lower()
if character in vowel:
    print(f"the given character is vowel.")
else:
    print(f"the given character is not a vowel.")