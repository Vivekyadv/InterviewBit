# Given array and a value, remove all the instances of that value
# return no of elements left after operations

# Method 1: use list comprehension
def solve(arr, val):
    arr[:] = [x for x in arr if x != val]
    return len(arr), arr

arr = [1,2,4,1,5,1,6]
print(solve(arr, 1))

# Method 2: use two pointer algo
# i --> prev ptr and j --> next ptr
# if arr[j] != val: store arr[j] in arr[i] and then inc i
# inc j
def solve(arr, val):
    i = j = 0
    while j < len(arr):
        if arr[j] != val:
            arr[i] = arr[j]
            i += 1
        j+=1
    arr[:] = arr[:i]
    return i, arr
arr = [1,2,5,3,6,1,5,1,3,5,4,6,3,1,4,1,1,4]
print(solve(arr, 1))
