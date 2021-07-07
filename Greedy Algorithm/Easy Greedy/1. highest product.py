# Given array. return highest product possible by multiplying 3 elements from array

# arr = [0, -1, 3, 100, 70, 50]     ans = 100*70*50 = 35000
# arr = [0, -1, 3, 100, -70, -50]   ans = 100*(-70)*(-50) = 3500

# clearly simply taking product of max 3 element will not work, as product of 2 -ve numbers
# are +ve so we need to take maximum of (product of max 3 elements) 
# and (product of min 2 (-ve elements) and max 1 element)

# Method 1: sort array and return max of (product of last 3 elements) and 
# (product of first 2 and last elements)
def solve(arr):
    arr.sort()
    p1 = arr[-1]*arr[-2]*arr[-3]
    p2 = arr[0]*arr[1]*arr[-1]
    return max(p1, p2)

arr = [0, -1, 3, 100, 70, 50]
print(solve(arr))

# Method 2: instead of sorting the array, we can take max 3 elements and 
# (two min element and one max element of array) in single iteration
def solve(arr):
    maxA = maxB = maxC = -pow(2,32)
    minB = minC = pow(2,32)

    for i in range(len(arr)):
        if arr[i] > maxA:
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
        elif arr[i] > maxB:
            maxC = maxB
            maxB = arr[i]
        elif arr[i] > maxC:
            maxC = arr[i]
        
        if arr[i] < minB:
            minC = minB
            minB = arr[i]
        elif arr[i] < minC:
            minC = arr[i]
    
    p1 = maxA * maxB * maxC
    p2 = maxA * minB * minC

    return max(p1, p2)

arr = [0, -1, 3, 100, -70, -50]
print(solve(arr))
