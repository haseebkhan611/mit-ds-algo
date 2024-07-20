

def sumArray(arr):
    if len(arr) == 0: return [-1]
    if len(arr) == 1: return arr[0]
    return (sumArray(arr[:-1]) + arr[-1])

if __name__ == "__main__":
    arr = [5,5,10]
    print(sumArray(arr))