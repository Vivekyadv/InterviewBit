# Given an array, representing seats in each row of a stadium. You need to sell tickets to
# B people. Each seat costs equal to the number of vacant seats in the row it belongs to. 
# The task is to maximize the profit by selling the tickets to B people.

# Example: arr = [1, 4], B = 2
# sell 1st ticket in 2nd row --> 4,     now arr = [1, 3]
# sell 2nd ticket in 2nd row --> 3,     now arr = [1, 2]
# ans = 4 + 3

# Method 1: find max in array and add it in result, decrement it and B.
def solve(arr, B):
    profit = 0
    while B > 0:
        max_ele = max(arr)
        indx = arr.index(max_ele)
        profit += max_ele

        arr[indx] -= 1
        B -= 1

    return profit

arr = [10, 4, 6, 3, 5, 7]
B = 6
print(solve(arr, B))  


# Same approach using heap, we use min heap so take -ve of all array elements
from heapq import *
def solve(arr, B):
    profit = 0
    arr = [-x for x in arr]
    heapify(arr)

    for i in range(B):
        smallest = arr[0]
        heapreplace(arr, arr[0] + 1)
        profit += abs(smallest)
    
    return profit

arr = [10, 4, 6, 3, 5, 7]
B = 6
print(solve(arr, B))  
