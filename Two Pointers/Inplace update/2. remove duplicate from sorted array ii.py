# Given sorted array, remove duplicate in place such that each ele 
# can appear atmost twice and return its length. 
# Note: Do not allocate extra space for another array

# Method 1: use 2 pointers, one to scan array and other only move 
# if condition is satisfied (arr[j-1] != arr[i] or arr[j-2] != arr[i])
def removeDuplicates(arr):
    j = i = 2
    while i < len(arr):
        if arr[j-1] != arr[i] or arr[j-2] != arr[i]:
            arr[j] = arr[i]
            j += 1
        i += 1
    arr = arr[:j]
    return j, arr

arr = [1,1,1,2,5,8,8,8,8,8,10]
print(removeDuplicates(arr))


arr = [1,1,1,2,5,8,8,8,8,8,10]
def solve(arr):
    indx = count = 0
    prev = arr[0]
    k = 2
    for i in range(len(arr)):
        if arr[i] == prev:
            count += 1
            if count <= k:
                arr[indx] = prev
                indx += 1
        else:
            count = 1
            prev = arr[i]
            if count <= k:
                arr[indx] = prev
                indx += 1
    arr = arr[:indx]
    return indx, arr

print(solve(arr))