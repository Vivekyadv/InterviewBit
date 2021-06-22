# Given an array A of integers, find index of values that satisfy A + B = C + D, where 
# A, B, C and D are integers. return the indices of A, B, C, D (i, j, k, l)
# conditions:  i < j,   k < l,   i < k,   j != l and j != k   


# Method 1: using nested loop, calculate sum = arr[i] + arr[j]
# if this sum not exist in table, then add in table with its indices (i, j)
# if exist in table then, at this moment, we're traversing with (k, l), now check
#    if i < k and j not in (k, l)   [ i.e j != k and j != l] 
#       add (i, j, k, l) in result

def equal(arr):
    seen = {}
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum not in seen:
                seen[sum] = (i, j)
            else:
                a = seen[sum][0]
                b = seen[sum][1]
                if a < i and b not in (i, j):
                    result.append([a, b, i, j])
    result.sort()
    return result[0]

arr = [3, 4, 7, 1, 2, 9, 8]
print(equal(arr))


# Method 2
def equal(A):
    pairsSum = {}
    equals = []
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            sum = A[i] + A[j]
            if sum in pairsSum:
                temp = pairsSum[sum][-1]
                if i not in temp and j not in temp:
                    pairsSum[sum].append([i,j])
            else:
                pairsSum[sum] = [[i,j]]

            if len(pairsSum[sum])==2:
                x = pairsSum[sum][0]
                y = pairsSum[sum][1]
                equals.append(x + y)
    
    equals.sort()
    return equals[0]

print(equal(arr))
