# Given array of integers, find two numbers such that there sum = target num
# return their indices (indx1 < indx2). if there exist multiple solutions then return
# minimum indx2. and if for minimum indx2 there still exist multiple solutions then 
# return mininum indx1. indices is not 0-based index

# Example: [2, 3, 2, 7, 5, 7, 8, 12]  target = 9
# possible soln: [0,3], [0,5], [2,3] and [2,5] return arr[0] + arr[3], i.e. return [1,4]

# Note we can't use brute force method 'cause it'll give minimum indx1 but priority 
# should be min indx2

# Method: using hasmap, for each iteration
# store number and its index in dict()  and check if target-num is present in dict()

def twoSum(arr, target):
    check = {}
    for i in range(len(arr)):
        num = arr[i]
        compOfnum = target-num
        if compOfnum in check:
            return [check[compOfnum]+1, i+1]
        else:
            if num not in check:
                check[num] = i
    return []

arr = [1, 7, 2, 4, 4, 4, 3, -5, -3, 9, 7, 8, 6, 12]
target = 7
print(twoSum(arr, target))
