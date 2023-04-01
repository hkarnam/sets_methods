# python program to count the number of vowels present in a string using sets:


str1 = input('Enter a string')
vowels = set('aeiou')
count = 0

for letter in str1.lower():
    if letter in vowels:
        count += 1
print(f"Number of vowels present in a string are: {count}")
