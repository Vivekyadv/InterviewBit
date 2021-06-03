# Given array of integers, every element appears twice except one.
# Find that element

# Method 1: using mathmatics
# arr = [a,a,b,b,c,c,d]
# Logic:  2*(a+b+c+d) - sum(arr) = d
def singleNumber(arr):
    return 2 * sum(set(arr)) - sum(arr)

arr = [12,3,7,4,7,3,4]
print(singleNumber(arr))

# Method 2: using counter
from collections import Counter
def singleNumber(arr):
    count = Counter(arr)
    for ele in count:
        if count[ele] == 1:
            return ele

print(singleNumber(arr))

# Method 3: sorting + linear traversal
# sort the array, then check if adjacent elements are same or not.
def singleNumber(arr):
    arr.sort()
    i, j = 0, 1
    while (j < len(arr)):
        if arr[i] == arr[j]:
            i += 2
            j += 2   
        else:
            return arr[i] 
    return arr[i]

print(singleNumber(arr))

# Method 4: using XOR operator
# XOR of same number is 0, if we find XOR of whole array, then 
# onlyl number left is num with single occurence
def singleNumber(arr):
    res = 0
    for i in range(len(arr)):
        res = res ^ arr[i] 
    return res

print(singleNumber(arr))