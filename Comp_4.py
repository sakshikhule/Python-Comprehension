#4. Remove all of the vowels in a string (take input from user) 
inp = input("Enter string: ")
vow = 'aeiouAEIOU'
num = ' '.join(char for char in inp if char not in vow)
print(num)
