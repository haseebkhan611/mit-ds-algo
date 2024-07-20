# Base Case: n == 0
# Smallest prob: Remainder + Binary(next_Step)


def convertA(n):

    # if n >= 1:
    #     convertA(n // 2)
    # print(n % 2, end = '\n')
    if n == 0:
        return '0'
    else:
        return convertA(n//2) + str(n%2)
    

if __name__ == "__main__":
    decimal = 233
    result = ""
    print(convertA(decimal))