# Array A, find if an integer p exists in the array such that the 
# number of integers greater than p in the array equals to p.

# Algorithm:
# step 1: sort array
# step 2: if A[-1] == 0: return 1
# step 3: check each element with no of element greater than that (n-1-i)
#         and if A[i] == A[i+1] skip it

def solve(A):
    n = len(A)
    A.sort()
    if A[-1] == 0:
        return 1
    for i in range(n):
        count = n-1-i
        if A[i] != A[i+1] and A[i] == count:
            return 1
    return -1

print(solve([1,2,3,3]))
print(solve([1-5,-6,0,-2,-1]))