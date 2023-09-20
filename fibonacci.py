def fibonacci(n):
    a = 0
    b = 1
    
    if n<0:
        print("incorrect input!")
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

    
def fibo_recursive(n):
    if n<=1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)