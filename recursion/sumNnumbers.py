'''
n = 10
sum = 1+2+3+4+5+6+7+8+9+10 = 55

RECURSION:
Base Case: we have return 1
Smallest Case: Sum(n) + Previous_SUm
'''

def findSum(n):
    if n == 1:
        return 1
    else:
        return (findSum(n-1) + n)


if __name__ == "__main__":
    n = 11
    y = findSum(n)
    print(y)