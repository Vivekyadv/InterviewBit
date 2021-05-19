# Given an unsorted integer array, find the 1st missing positive int

# Algorithm:
    # step 1: Extract element 1 to n+1 from given array becoz missing number 
    #         would be in range 1 to n+1
    # step 2: The answer will be N+1 only if all of the elements of the array 
    #         are exact one occurrence of [1, N].
    # step 3: Sort them
    # step 4: Compare number with its index i+1


def solution(A):
    miss_arr = [x for x in A if x > 0 and x < len(A)]
    miss_arr.sort()
    for i in range(len(miss_arr)):
        if miss_arr[i] != i+1:
            return i+1
    return len(miss_arr) + 1

arr = [3,4,-1,1,9]
print(solution(arr))


# Algorithm:
    # array = [3,4,-1,1,9]
    # step 1: convert to [3,4,6,1,6] :::: if num <= 0 or > n ---> A[i] = n+1
    # step 2: mark the index we visited using -ve sign
    #         index = num-1
    # step 3: then extract the index of number > 0


def solve(A):

    # cleaning up the array
    for i in range(len(A)):
        if A[i] <= 0 or A[i] > len(A):
            A[i] = len(A)+1
    print(A)

    # place marker
    for num in A:
        num = abs(num)
        if num <= len(A) and A[num-1] >= 0:
            A[num-1] *= -1
    
    # final step
    for i in range(len(A)):
        if A[i] > 0:
            return i + 1
    return len(A) + 1

print(solve([3,4,-1,1,9]))
