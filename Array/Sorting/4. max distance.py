# # Given array, find max of j-i for which A[i] <= A[j] 

# def leftmin(arr, n):
#     left_min = [0]* n
#     left_min[0] = arr[0]
#     for i in range(1, n):
#         left_min[i] = min(left_min[i-1], arr[i])
#     return left_min

# def rightmax(arr, n):
#     right_max = [0]* n
#     right_max[n-1] = arr[n-1]
#     for i in range(n-2, -1, -1):
#         right_max[i] = max(right_max[i+1], arr[i])
#     return right_max
            
# def maximumGap(A):
#     if not A:
#         return -1
#     n = len(A)
#     leftMin = leftmin(A, n)
#     rightMax = rightmax(A, n)
#     print("Leftmin", leftMin)
#     print("RightMAx", rightMax)

#     minI = maxJ = 0
#     currMax = 0
#     while minI < n and maxJ < n:
#         lmin, rmax = leftMin[minI], rightMax[maxJ]
#         if lmin <= rmax:
#             currMax = max(currMax, maxJ - minI)
#             maxJ += 1
#         else:
#             minI += 1
    
#     return currMax


# arr = [5,6,1,4,2,3]
# print(maximumGap(arr))



def solve(A):
    n = len(A)
    array = list(range(n))
    
    array.sort(key= lambda i: A[i])
    maxDistance = 0
    minSofar = array[0]
    for i in array:
        if i <= minSofar:
            minSofar = i
        else:
            maxDistance = max(maxDistance,i - minSofar)
    return maxDistance




arr = [3,3,4,5,2]
# 2 3 3 4 5 ---> 4 0 1 2 3
solve(arr)
