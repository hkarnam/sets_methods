# python program that Displays which letters are in the First string but not in the second

str1 = set('sun is out today')
str2 = set('that is a pretty rainbow')

letters_diff = str1.difference(str2)
print(f"Letters in the first string but not in second string are: {letters_diff}")

# for loop just to represent the letters when there are also space in between

for element in letters_diff:
    print(element)