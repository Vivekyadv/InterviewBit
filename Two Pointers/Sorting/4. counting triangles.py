# Given an array, find no of △s formed using 3 elements of
# array. Logic: sum of 2 sides > 3rd side

# Method 1: use 3 nested loops. Each loop starting from indx of prev
# loop to the end of array.
# check i + j > k, i + k > j and j + k > i. all 3 comditions must
# be matched. if so, increment count

def solve(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i] + arr[j] > arr[k]) and \
                    (arr[i] + arr[k] > arr[j]) and \
                    (arr[j] + arr[k] > arr[i]):
                    count += 1
    return count % (10**9+7)

arr = [10, 21, 22, 100, 101, 200, 300 ]
print(solve(arr))


# Method 2: using two pointer method
# sort the array, run loop from n to 1, take j = 0 and k = i-1.
# while j < k, do the following
# 1. now if △ can be formed using A[j], A[k] and A[i] then △s can
#    obv formed from (A[j+1], A[j+2] ... A[k-1]), A[k] and A[i]
#    so, ans += k-j and then dec the value of k
# 2. if triangle can't be formed using A[j], A[k] and A[i] then inc j

def solve(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n-1,0,-1):
        j = 0
        k = i-1
        while j < k:
            if arr[j] + arr[k] > arr[i]:
                count += k-j
                k -= 1
            else:
                j += 1
    return count

arr = [4, 7, 3, 6, 5]
print(solve(arr))