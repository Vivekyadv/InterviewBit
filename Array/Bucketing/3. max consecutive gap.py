# Given an unsorted array, find the maximum difference between 
# the successive elements in its sorted form.
# use linear time complexity (dont use sort())

# Algorithm: pigeonhole sorting

def max_gap(A):
    n = len(A)
    A.sort()
    maxx = 0
    for i in range(n-1):
        maxx = max(maxx, A[i+1]-A[i])
    return maxx

arr = [5,1,10]
print(max_gap(arr))


from math import ceil
def maximumGap(A):
    n = len(A)
    if n < 2:
        return 0
    max_ele, min_ele = max(A), min(A)

    interval = int(ceil( (max_ele-min_ele) / (n-1) ))
    MIN_VALUE, MAX_VALUE = -1, float("inf")
    bucketMin, bucketMax = [MAX_VALUE]*(n-1), [MIN_VALUE]*(n-1)
    for i in range(n):
        if A[i] not in [max_ele, min_ele]:
            index = int( (A[i] - min_ele) / interval)
            bucketMin[index] = min(bucketMin[index], A[i])
            bucketMax[index] = max(bucketMax[index], A[i])
    
    previous_max = min_ele
    max_gap = 0
    for i in range(len(bucketMax)):
        if bucketMax[i] != -1:
            max_gap = max(max_gap, bucketMin[i]-previous_max)
            previous_max = bucketMax[i]
    
    max_gap = max(max_ele-previous_max, max_gap)

    return max_gap

print(maximumGap([3,6,9,1,18]))

a = float("infinity")
print(a, type(a))