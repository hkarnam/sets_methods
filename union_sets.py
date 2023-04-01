# python program that displays which letters are present in both the strings

string1 = input('first string is: ')
string2 = input('second string is: ')

str3 = set(string1).union(set(string2))
print(str3)

for x in str3:
    print(x)