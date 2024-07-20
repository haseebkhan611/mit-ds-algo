'''
find if x is in array

Base Case: 
    - if x == arr[mid]: return mid
    - if left > right: return -1
Smallest Prob:
    - if x < arr[mid]: return binSearch(arr, x, left, mid - 1)
    - else: return binSearch(arr, x, mid+1, right)
'''

def binSearch(arr,x, left, right):
    if left >= right:
        return -1;
    mid = (left + right) // 2
    # print(mid)

    if x == arr[mid]: return mid;
    if(x < arr[mid]): return(binSearch(arr,x,left,mid))
    else: return(binSearch(arr,x,mid+1,right))


if __name__ == "__main__":
    x = 20
    arr = [0,1,2,3,4,7,9,10,20,30]
    low = 0
    high = len(arr) - 1
    print(binSearch(arr,x,low,high))