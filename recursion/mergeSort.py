


def merge(arr, mid, left, right):
    

def mergeSort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    mergeSort(arr, mid+1, right)
    mergeSort(arr, left, mid)
    merge(arr, mid, left, right)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    left = 0
    right = len(arr) - 1
    y = mergeSort(arr, left, right)
    print(y)