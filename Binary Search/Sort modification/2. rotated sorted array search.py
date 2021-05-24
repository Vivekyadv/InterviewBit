# Given an array and integer key. The array is rotated at some pivot 
# element (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 )
# Find if key element is present in array using lon(n) Time complexity

def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def search(arr, key):
    pivot_indx = -1
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if mid < end and arr[mid] > arr[mid+1]: 
            pivot_indx = mid
            break
        if mid > start and arr[mid] < arr[mid - 1]:
            pivot_indx = mid-1
            break
        if arr[start] >= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    if pivot_indx == -1:
        return binary_search(arr, key, 0, len(arr)-1)
    if arr[pivot_indx] == key:
        return pivot_indx
    if arr[0] <= key:
        return binary_search(arr, key, 0, pivot_indx-1)
    return binary_search(arr, key, pivot_indx+1, len(arr)-1)

arr = [101,103,106,109,158,164,182,187,202,205,2,3,32,57,69,74,81,99,100]
key = 202
print(search(arr, key))

# Method 2: we can directly find key using binary search in one go

def search(arr, key):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < arr[end]:
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

print(search(arr, key))
