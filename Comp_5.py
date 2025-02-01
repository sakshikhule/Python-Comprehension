#5. Find all of the words in a string that are less than 5 letters (take input from user) 
inp = input("Enter string: ")
string = [char for char in inp.split() if len(char) < 5]
print(string)
