# Given an array and integer B. find total no of subarrays having exactly B odd numbers
# arr = [4, 3, 2, 3, 4]   B = 2
# subarrays = [4, 3, 2, 3], [4, 3, 2, 3, 4], [3, 2, 3], [3, 2, 3, 4]

# Method 1: generate all possible subarrays and check for subarrays having B odds
# Time complexity: O(n^2)

def solve(arr, val):
    count = 0
    for i in range(len(arr)):
        odds = 0
        for j in range(i, len(arr)):
            if arr[j] % 2 == 1:
                odds += 1
            
            if odds == val:
                count += 1
    return count

arr = [4, 3, 2, 3, 4]
val = 2
print(solve(arr, val))


# Method 2: for every position i, count no_of_subarr ending at i that have B odd numbers
# increment prefix of no_of_odds encounter till now
# at each moment, check no_of_odds >= B: if so, countsubarr += prefix[odd-k]

def solve(arr, val):
    n = len(arr)
    count = 0
    prefix = [0] * (n+1)
    odd = 0
 
    for i in range(n):
        prefix[odd] += 1
 
        if arr[i] % 2 == 1:
            odd += 1
 
        if odd >= val:
            count += prefix[odd - val]
 
    return count

arr = [2,2,2,1,2,2,1,2,4,3,3,2]
print(solve(arr, val))
