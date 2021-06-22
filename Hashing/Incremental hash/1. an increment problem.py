# Given array of integers. while iterating the numbers in array, increase the 1st occurance of 
# num by 1 and incluse this in ans

# Example: arr = [1, 1, 1, 2, 2, 3, 4]
# i = 0   num = 1     ans = 1
# i = 1   num = 1     ans = 2 1   (since num = 1 is at indx 0, inc it by 1 and store in ans)
# i = 2   num = 1     ans = 2 2 1
# i = 3   num = 2     ans = 3 2 1 2
# i = 4   num = 2     ans = 3 3 1 2 2
# i = 5   num = 3     ans = 4 3 1 2 2 3
# i = 6   num = 4     ans = 5 3 1 2 2 3 4


# using another array to sotre the result       Time and Space complexity: O(n)
def solve(arr):
    ans = []
    for i in range(len(arr)):
        num = arr[i]
        if num in ans:
            indx = ans.index(num)
            ans[indx] += 1
        ans.append(num)
    return ans

arr = [1, 1, 1, 2, 2, 3, 4]
print(solve(arr))


# modify the given array        Time: O(n) and Space: O(1)
def solve(arr):
    for i in range (len(arr)):
        num = arr[i]
        indx = arr.index(num)
        if indx < i:
            arr[indx] += 1
    return arr

arr = [1, 1, 1, 2, 2, 3, 4]
print(solve(arr))
