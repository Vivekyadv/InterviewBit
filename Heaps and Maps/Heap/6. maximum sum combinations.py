# Given two equally sized arrays A, B. Return the maximum C valid sum combinations 
# from all the possible sum combinations.
# sum combinations -> one element from A and one from B

# Example: A = [1, 2, 3, 4]   B = [1, 2, 5, 6]   C = 4
# (4, 6) --> 10,   (4, 5) --> 9,   (3, 6) --> 9,   (3, 5) --> 8
# ans = 4


# Method 1: Brute force approach, take all possible combinations and insert them to 
# a max heap. after inserting all the combinations, we take out C elements from heap
# that would be the result.

from heapq import *
def solve(A, B, C):
    pq = []
    result = []
    for i in range(len(A)):
        for j in range(len(B)):
            currSum = A[i] + B[j]
            heappush(pq, -currSum)
    
    for x in range(C):
        sumAtTop = heappop(pq)
        result.append(-sumAtTop)
    return result

A = [4, 2, 5, 1]
B = [8, 0, 3, 5]
C = 3
print(solve(A, B, C))


# Method 2: sort the arrays, use heap to store sum
# 1. create a heap to store the sum of elements of both arrays along with their indices.
# 2. initialise heap with max sum (sum of last elements of arrays) with their indices
# 3. now in a loop till C, pop the heap and store sum in result, and check for (i-1, j) 
#    and (i, j-1), store sum in heap and add indices in seen

def solve(A, B, C):
    A.sort()
    B.sort()
    pq, result = [], []
    seen = set()
    
    i, j = len(A)-1, len(B)-1
    heappush(pq, [-(A[i]+B[j]), (i,j)])
    seen.add((i,j))
    
    for x in range(C):
        summ, (i,j) = heappop(pq)
        result.append(-summ)
        
        if i > 0 and (i-1, j) not in seen:
            currSum = A[i-1] + B[j]
            heappush(pq, [-currSum, (i-1, j)])
            seen.add((i-1,j))
            
        if j > 0 and (i,j-1) not in seen:
            currSum = A[i] + B[j-1]
            heappush(pq, [-currSum, (i,j-1)])
            seen.add((i,j-1))
    
    return result

A = [4, 2, 5, 1]
B = [8, 0, 3, 5]
C = 3
print(solve(A, B, C))
