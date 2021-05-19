# Find out if any integer occurs more than n/3 times in the array 
# In linear time complexity and constant space complexity
#
# Algorithm used: Moore voting algorithm

import sys
def findCandidate(A):
    candidate1, candidate2 = sys.maxsize, sys.maxsize
    count1, count2 = 0, 0

    for i in range(len(A)):
        if candidate1 == A[i]:
            count1 += 1
        elif candidate2 == A[i]:
            count2 += 1

        elif count1 == 0:
            candidate1 = A[i]
            count1 += 1
        elif count2 == 0:
            candidate2 = A[i]
            count2 += 1
        
        else:
            count1 -= 1
            count2 -= 1
        
    
# isMajority
    count1, count2 = 0, 0
    for i in range(len(A)):
        if A[i] == candidate1:
            count1 += 1
        elif A[i] == candidate2:
            count2 += 1
    if count1 > len(A)/3:
        return candidate1
    elif count2 > len(A)/3:
        return candidate2
    
    return -1

arr = [ 2, 1, 3, 1, 5, 1, 7 ]
print(findCandidate(arr))
