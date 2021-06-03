# Given array of integers, every element appears thrice except one.
# Find that element

# Method 1: using mathmatics
# arr = [a,a,a,b,b,b,c,c,c,d]
# Logic: [ 3*(a+b+c+d) - sum(arr)] // 2 = d

# Note: If the numbers in arr is large, then this method won't work

def singleNumber(arr):
    return ( 3*(sum(set(arr))) - sum(arr) )//2

arr = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(singleNumber(arr))

# Method 2: using Counter
from collections import Counter
def singleNumber(arr):
    count = Counter(arr)
    for ele in count:
        if count[ele] == 1:
            return ele

print(singleNumber(arr))

# Method 3: sorting + linear traversal
def singleNumber(arr):
    arr.sort()
    i, j = 0, 1
    while (j < len(arr)):
        if arr[i] == arr[j]:
            i += 3
            j += 3   
        else:
            return arr[i] 
    return arr[i]

print(singleNumber(arr))

# Method 4: count set bits of same position of all elements of array, 
# if count % 3 != 0 that means our result contains set bit at that pos
def singleNumber(arr):
    n = len(arr)
    ans = 0
    for i in range(32):
        summ = 0
        shift = 1<<i
        for j in range(n):
            if arr[j] & shift:
                summ += 1

        if summ % 3 != 0:
            ans += shift
    return ans

print(singleNumber(arr))