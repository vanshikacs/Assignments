def pattern(n):
    for i in range(n):  
        
        for j in range(n - i):
            print(chr(65 + j), end=' ')
        
    
        for j in range(2 * i - 1):
            print(' ', end=' ')
        
        
        for j in range(n - i - 1, -1, -1):
            print(chr(65 + j), end=' ')
        
        print()

n = int(input("Enter the number of rows: "))
pattern(n)
