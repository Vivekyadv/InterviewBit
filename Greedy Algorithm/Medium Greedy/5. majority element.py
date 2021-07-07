# Given array of integers, find the majority element. Majority element is the element that
# appears more than N/2 times.
# Note: assume the array is non-empty and majority element always exist in array.
# Similar to N/3 Repeat Number question from Array


# Method 1: iterate through the array and count number of occurence of each element
# then check which element occers more than N/2

from collections import Counter

def majorityElement(arr):
    n = len(arr)
    count = Counter(arr)
    for ele in arr:
        if count[ele] > n//2:
            return ele
    
arr = [1, 2, 1, 1, 1, 4, 1, 5, 1, 6]
print(majorityElement(arr))


# Method 2: sort the array and check for every element
# ith element should be equal to (n/2)th element from i
def majorityElement(arr):
    arr.sort()
    l = len(arr)//2
    for i in range(len(arr)):
        if arr[i] == arr[i+l]:
            return arr[i]

# Or just return arr[l], as majority element should always lie in the mid of array
# Condition: majority element should be present in array and array must be non-empty
print(majorityElement(arr))


# Method 3: Moore's Voting algorithm
def majorityElement(arr):
    count = 1
    majEle = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == majEle:
            count += 1
        else:
            count -= 1
        if count == 0:
            majEle = arr[i]
            count = 1

    return majEle   

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majorityElement(arr))
