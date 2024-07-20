'''
n = 5
fib = 1+1+2+3+5+8+13+21 
Base Case: n = 2 || n = 1 -> return 1
Smallest prob: return fib(n-1) + fib(n-2)
'''

def fib(n):
    if (n == 1 or n == 2) and (n > 0):
        return 1
    else:
        return (fib(n-1) + fib(n-2))


if __name__ == "__main__":
    n = 8
    y = fib(n)
    print(y)