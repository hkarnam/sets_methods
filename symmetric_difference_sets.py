# python program that displays which letters are in two strings  but not in both:

str1 = set('wonder what day it is today?')
str2 = set('How long does it take to make a coffee?')

unique_letters = str1.symmetric_difference(str2)
print(unique_letters)

for x in unique_letters:
    print(x)
