# given NxM matrix with each row sorted, find the overall median of it
# Note: no extra space is allowed

# Method 1: store the matrix in 1D array --> sort the array and return 
# the median. 
# Time complexity = O(mnxlog(mn))
# Space complexity = O(mn)

def findMedian(arr):
    rows = len(arr)
    temp_arr = []
    for i in range(rows):
        temp_arr += arr[i]
    temp_arr.sort()
    n = len(temp_arr)
    if n % 2 == 1:
        return temp_arr[n//2]
    else:
        med1 = temp_arr[(n+1)//2]
        med2 = temp_arr[(n-1)//2]
        return (med1+med2) //2

arr = [
    [1,3,5],
    [2,6,9],
    [3,6,9]
]
print(findMedian(arr))

# Method 2: using binary search
# Note: median is (1+ nxm)/2 th smallest element. So for x to be median
# there should be (n*m)/2 elements smaller than x

# Algorithm: 
# Step 1: Find the min and max elements of matrix. 
# Step 2: Then use binary search from min to max and get a count of 
#         elements < mid and accordingly change the min or max.
# Step 3: For every element x, count no_of_elements smaller than x by 
#         using upper_bound()
#         if count < target_count:
#             median must be > the selected number
#         else: median must be <= the selected number. 

from bisect import bisect_right as upper_bound

def findMedian(arr):
    n = len(arr)
    m = len(arr[0])

    # Find min and max element of matrix
    min_el, max_el = arr[0][0], 0
    for i in range(n):
        min_el = min(min_el, arr[i][0])
        max_el = max(max_el, arr[i][-1])
    
    target = (1 + n*m) // 2
    
    while min_el <= max_el:
        mid = min_el + (max_el - min_el) // 2
        count = 0

        # count no_of_elements smaller than mid
        for i in range(n):
            count += upper_bound(arr[i], mid)
        if count < target:
            min_el = mid + 1
        else:
            max_el = mid - 1
    return	min_el
    
print(findMedian(arr))
