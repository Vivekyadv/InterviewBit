# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# 1. Each child must have at least one candy.
# 2. Children with a higher rating get more candies than their neighbors.

# EXample: arr = [3, 5, 8, 2, 5, 4]

# break this question in two parts, in one part we'll check only left neighbor and in 
# other part, we'll check only right neighbor.

def solve(arr):
    n = len(arr)
    left = [1]*n
    right = [1]*n

    for i in range(n-1):
        if arr[i+1] > arr[i]:
            left[i+1] = left[i] + 1
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            right[i] = right[i+1] + 1
    
    result = []
    for i in range(n):
        result.append(max(left[i], right[i]))
    return (result)

arr = [3, 5, 8, 2, 5, 4]
print(solve(arr))
    

# Solution 2
def solve(arr):
    n = len(arr)
    candies = [1]*n
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candies[i+1] = candies[i] + 1
    
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i] and candies[i-1] <= candies[i]:
            candies[i-1] = candies[i] + 1

    return candies

arr = [12, 4, 3, 11, 34, 34, 1, 67]
print(solve(arr))

