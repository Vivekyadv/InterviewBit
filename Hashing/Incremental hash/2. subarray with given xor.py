# Given an array of integers A and an integer B.
# Find the total number of subarrays having bitwise XOR of all elements equals to B.

from collections import defaultdict
def solve(a, b):
    c = defaultdict(int)
    c[0] = 1
    xor = res = 0
    for i in range(len(a)):
        xor ^= a[i]
        res += c[xor^b]
        c[xor] += 1
    return res

arr = [4, 2, 2, 6, 4]
val = 6
print(solve(arr, val))

def solve(arr, val):
    count = xor = 0
    hashmap = {0:1}
    for i in range(len(arr)):
        xor ^= arr[i]
        if xor ^ val in hashmap:
            count += hashmap[xor^val]
            
        if xor not in hashmap:
            hashmap[xor] = 1
        else: hashmap[xor] += 1
    
    return count

print(solve(arr, val))
