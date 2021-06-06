 # Given two sorted array, merge them (in sorted order)
 # Try to do in constant space complexity


# Method 1: use the idea of merge func of merge sort
def solve(arr1, arr2):
    i = j = 0
    m = len(arr1)
    n = len(arr2)
    arr = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j += 1
    
    # copy remaining elements
    if i < m:
        arr += arr1[i:]
    elif j < n:
        arr += arr2[j:]
    return arr

arr2 = [2,3,5,6,9,12,14]
arr1 = [4,5,8]
print(solve(arr1, arr2))

# Time and Space complexity : O(m+n)

# Method 2: using built-in function 
def merge(arr1, arr2):
    arr1 [:] = sorted(arr1 + arr2)
    # or arr1.extend(arr2) --> or arr1 += arr2
    # arr1.sort()
    return arr1

arr1 = [-4,3]
arr2 = [-2,-2]
print(merge(arr1, arr2))


# Method 3: Extend 1st array, and compare elements of 1st and
# 2nd array from the end. k starts from end of merged array
# if arr1[i] > arr2[j] : arr1[k] = arr1[i]
# else arr1[k] = arr2[j]. Then dec (i,k) or (j,k) accordingly
# take care of remaining elements (either of arr1 or arr2)

def merge(arr1, arr2):
    i = len(arr1)-1
    j = len(arr2)-1
    arr1.extend(arr2)
    k = len(arr1)-1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    while i >=0:
        arr1[k] = arr1[i]
        i -= 1
        k -= 1
    return arr1

arr1 = [2,3,5,6,9,12,14]
arr2 = [4,5,8]
print(merge(arr1, arr2))