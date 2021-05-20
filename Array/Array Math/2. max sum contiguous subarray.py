# Given integer array, find subarray having maximum sum
# Algorithm: Kadane's Algo
# iterate array and store the sum of elements, when this sum < 0,
# start storing the sum again from 0 (initialise the sum = 0)


def maxSubArray(A):
    sum_subarray = 0
    max_sum = A[0]
    for i in range(len(A)):
        sum_subarray += A[i]
        max_sum = max(sum_subarray, max_sum)
        if sum_subarray < 0:
            sum_subarray = 0
    return max_sum

arr = [-4,1,3,-2,6,2,-1,-4,-7]
print(maxSubArray(arr))
