#6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)
inp = input("Enter string: ")
string = {x:len(x) for x in inp.split()}
print(string)
