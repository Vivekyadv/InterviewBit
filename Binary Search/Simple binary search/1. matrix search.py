# Given a 2D matrix, search element in matrix and return 1 if it found
# else return 0 


def binary_search(arr , key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end -start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid -1
    return -1

# Method 1: create a new array with elements in matrix and the search 
# using binary search ::: 
# Time complexity = O(n) to create array and O(lon(mxn) for binary search

def searchMatrix(arr, key):
    row = len(arr)
    temp = []
    for i in range(row):
        temp += arr[i]
    
    return 1 if binary_search(temp, key) != -1 else 0

arr = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
]
print(searchMatrix(arr, 23))

# Method 2: use Binary search in 2D martix

def searchMatrix(arr, key):
    start = 0 
    end = len(arr)-1
    while start < end:
        mid = start + (end-start)//2
        if arr[mid][0] <= key:
            if key <= arr[mid][-1]:
                start = mid
                break
            start = mid + 1
        else:
            end = mid -1
    return 1 if binary_search(arr[start], key) != -1 else 0

print(searchMatrix(arr,45))