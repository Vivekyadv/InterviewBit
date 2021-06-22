# Find the largest continuous sequence in a array which sums to zero.
# Example: Input:  [2, 8, -3, -5, 2, -4, 6, 1, 2, 1, -3, 4] 
# Output: [-3, -5, 2, -4, 6, 1, 2, 1]

# Explanation: possible answers are [8,-3,-5], [2,8,-3,-5,2,-4], [-5,2,-4,6,1],
# [-3,-5,2,-4,6,1,2,1], [-5,2,-4,6,1,2,1,-3] with max length = 8
# but [-3,-5,2,-4,6,1,2,1] occurs before [-5,2,-4,6,1,2,1,-3] so that's the ans 


# Logic: if sum(arr[i:j]) == sum(arr[i:k]) that means sum(arr[j:k]) = 0

# Method: using hash table, store sum till now with its index 
# if sum repeats (lets say sum = x), that means sum of subarray from 
# Previous_Occurrence_of_x to till now is zero (0)

def isZero(arr):
    prefixSum = {0:-1}
    total = 0
    start = end = -1
    for i in range(len(arr)):
        total += arr[i]
        if total not in prefixSum:
            prefixSum[total] = i
        else:
            currLen = i - prefixSum[total]
            prevLen = end - start
            if currLen > prevLen:
                start = prefixSum[total]
                end = i

    return arr[start+1:end+1]

arr = [2, 8, -3, -5, 2, -4, 6, 1, 2, 1, -3, 4]
print(isZero(arr))

