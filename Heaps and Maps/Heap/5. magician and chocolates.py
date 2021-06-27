# Given N bags, each bag contains Bi chocolates. There is a kid and a magician. 
# In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the 
# magician fills the ith bag with floor(Bi/2) chocolates.
# Find the maximum number of chocolates that kid can eat in t units of time.

# Note: this is similar to profit maximization
# instead of B[i] -= 1 (in profit max), we've to (B[i] = B[i]//2)

# Method 1: find max in array and add it in result, decrement t and arr[i] = arr[i]//2
def solve(arr, t):
    mod = 10**9 + 7
    result = 0
    
    while t > 0:
        max_ele = max(arr)
        indx = arr.index(max_ele)
        result += max_ele

        arr[indx] = arr[indx] // 2
        t -= 1

    return result%mod

arr = [2, 4, 6, 8, 10]
t = 5
print(solve(arr, t))


# Same approach using heap, we use min heap so take -ve of all array elements
# take care of floor value of -ve integers
from heapq import *
def solve(arr, t):
    mod = 10**9 + 7
    result = 0
    arr = [-x for x in arr]
    heapify(arr)

    while t > 0:
        choco = arr[0]
        heapreplace(arr, -(-arr[0]//2))
        result += -choco
        t -= 1
    
    return result % mod

arr = [2, 4, 6, 8, 10]
t = 5
print(solve(arr, t))
