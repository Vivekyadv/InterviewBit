# Given a sorted array and a target value, return the index if the
# target value is found. If not, return the index where it would
# be if it were inserted in order

# Example: arr = [1,3,5,6,9] key = 5 ::: ans = 2
# arr = [1,3,5,6,9] key = 8 ::: ans = 4

def searchIndex(arr, key):
    start = 0
    end = len(arr)-1
    indx = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
            indx = mid
    return indx if indx != -1 else len(arr)

arr = [7, 13, 23, 34, 45, 76, 89]
key = 15
print(searchIndex(arr, key))

