#3. Count the number of spaces in a string (take input from user) 
inp = input("Enter string: ")
num = sum(1 for char in inp if char == ' ')
print(num)
