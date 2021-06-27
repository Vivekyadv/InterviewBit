# Given two arrays A & B of size N each. Find the maximum N elements from the 
# sum combinations (Ai + Bj) formed from elements in array A and B.

# Example:  A = [1,4,2,3]   B = [2,5,1,6]
# Maximum 4 elements of combinations sum are
# 10 -> (4+6),   9 -> (3+6),   9 -> (4+5),   8 -> (2+6)

# Method 1: Brute force approach, take all possible combinations and insert them to 
# a max heap. after inserting all the combinations, we take out N elements from heap
# that would be the result.


# Method 2: sort the arrays and the use heap to store sum with their indices 
# compare indices (i-1, j) and (i, j-1) with sum and store in heap accordingly

from heapq import *
def solve(A, B):
    A.sort()
    B.sort()
    n = len(A)
    pq, result = [], []
    seen = set()
    
    i, j = n-1, n-1
    heappush(pq, [-(A[i]+B[j]), (i,j)])
    seen.add((i,j))
    
    for x in range(n):
        Sum, (i,j) = heappop(pq)
        result.append(-Sum)
        
        if i > 0 and (i-1, j) not in seen:
            currSum = A[i-1] + B[j]
            heappush(pq, [-currSum, (i-1, j)])
            seen.add((i-1, j))
        
        if j > 0 and (i, j-1) not in seen:
            currSum = A[i] + B[j-1]
            heappush(pq, [-currSum, (i, j-1)])
            seen.add((i, j-1))

    return result

A = [1,4,2,3]   
B = [2,5,1,6]
print(solve(A,B))