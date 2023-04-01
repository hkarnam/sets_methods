# Python program to check common letters in two input strings..
str1 = input('enter first string: ')
str2 = input('enter second string: ')

common = set(str1).intersection(set(str2))
print(f'common letters of given two strings are: {common}')

for x in common:
    print(x)