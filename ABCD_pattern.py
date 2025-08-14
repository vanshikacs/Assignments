import string
n=int(input("Enter the number of rows:"))

for i in range(n):
    print(string.ascii_uppercase[:i+1])
