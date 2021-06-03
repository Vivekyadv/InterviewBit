# f(X, Y) = no of diff corresponding bits in binary representation
# of X and Y. 
# Example: f(2,7) = 2   ::: 2 = 010 and 7 = 111 --> diff bits = 2 

# Given array of n +ve int, find sum of f(arr[i], arr[j])

# Hint: 
# if arr[j] & 1: 
#   count += 1
# arr[j] = arr[j]>>1

def diffBits(arr, n):
    ans = 0
    mod = 10**9 + 7
    for i in range(32):
        count = 0
        for j in range(n):
            if arr[j] & 1<<i:
                count += 1
        ans += count * (n-count)*2
    return ans % mod

arr = [1,3,5]
print(diffBits(arr, len(arr)))