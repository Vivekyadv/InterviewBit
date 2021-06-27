# Given an 1D integer array A of size N you have to find and return the B largest 
# elements of the array A. 

# Example: arr = [11, 4, 6, 10, 3],     B = 2
# largest 2 elements = 11, 10


# Method 1: sort the array in reverse order and then return first B elements
def solve(arr, B):
    temp = sorted(arr, reverse=True)
    return temp[:B]         # or we can use return sorted(arr)[-B:]

arr = [11, 4, 6, 10, 3, 13, 9, 20, 14, 8, 15, 25, 21]
print(solve(arr, 6))


# Method 2: using heap  
# 1. store k elements in priorityQueue. 
# 2. after i == k, check if current element is > the peek element of priorityQueue. 
# if its greater, delete peek element from queue and add the current element in queue
#   Note: peek element is the smallest element in the queue

# 3. after the loop, remaining elements in the queue is answer
from heapq import *
def solve(arr, k):
    if k == len(arr):
        return arr

    pq = []
    for i in range(len(arr)):
        if i < k:
            heappush(pq, arr[i])
        elif arr [i] > pq[0]:
            heappop(pq)
            heappush(pq, arr[i])

    ans = []
    while len(pq) > 0 :
        ans.append(pq[0])
        heappop(pq)
    return ans

print(solve(arr, 6))

# using heapify
def solve(A, B):
    heapify(A)
    for i in range(len(A)-B):
        heappop(A)
    return A

print(solve(arr, 6))