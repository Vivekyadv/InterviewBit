# Find the kth row of pascal triangle
# Algorithm: 
# method 1: use DP to find nCr for each element
# method 2: use loop to find nCr for each element

def getRow(k):
    ans = []
    prev = 1
    for i in range(k+1):
        curr = (prev * (k-i)) // (i+1)
        ans.append(prev)
        prev = curr
    return ans

print(getRow(7))


def nCr(n, r):
    if(r > n - r):
        r = n - r
    res = 1
    for i in range(r):
        res = (res * (n-i)) // (i+1)
    return res

def solve(k):
    ans = []
    for i in range(k+1):
        ans.append(nCr(k,i))
    return ans

print(solve(7))


