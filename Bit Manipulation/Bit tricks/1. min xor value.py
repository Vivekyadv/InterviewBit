# Given array of int, find the min xor value of pairs in array
# Example:  arr = [9, 5, 3]
# 9 ^ 5 = 12
# 9 ^ 3 = 10
# 5 ^ 3 = 6         min xor value = 6

# Method 1: sort array and then find xor of pairs
def minXOR(arr):
    arr.sort()
    min_xor = 2**32-1
    val = 0
    for i in range(len(arr)-1):
        val = arr[i] ^ arr[i+1]
        min_xor = min(min_xor, val)

    return min_xor

arr = [5,3,9]
print(minXOR(arr))