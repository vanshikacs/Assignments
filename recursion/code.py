def num(n):
    if n > 0:  
        num(n - 1)  
        print(n)

num(5)
