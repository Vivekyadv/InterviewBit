# given sorted array of int, find starting and ending pos of given int
# Example: arr = [22,26,26,26,26,28,30] ::: ans = [1,4]

# Logic: use binary search 2 times... in first case, include key <= mid
# this will give the starting pos
# and in 2nd case, include key >= mid ---> this will give the ending pos 

def searchRange(arr, key):
    indx = [-1,-1]

    # 1st binary search
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if key <= arr[mid]:
            end = mid-1
        if key > arr[mid]:
            start = mid+1
    if arr[start] == key:
        indx[0] = start
    
    # 2nd binary search
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if key < arr[mid]:
            end = mid-1
        if key >= arr[mid]:
            start = mid+1
    if arr[end] == key:
        indx[1] = end
    return indx

arr = [1]
print(searchRange(arr,1))

arr = [23,24,24,24,27,27,30,31]
print(searchRange(arr,27))
