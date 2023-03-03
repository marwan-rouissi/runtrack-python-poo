# job 5

n = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(n):
    # condition de break
    if n <= 2:
        return 1
    
    else:
        
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(9))