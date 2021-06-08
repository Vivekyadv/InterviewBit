# Given 3 sorted array A, B and C
# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

# Example: A = [1, 4, 10]  B = [2, 15, 20]  C = [10, 12]
# ans = max(10-15, 15-10, 10-10) --> ans = 5

# Explanation: max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
# can be written as max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]), we 
# can varify this with any 3 integers

# now we have min and max, to reduce maximal difference(max-min), either
# increase the min element, or decrease the max element

# Method 1: increase the min element
def minimize(A, B, C):
    i = j = k = 0
    diff = 2**32-1
    while i < len(A) and j < len(B) and k < len(C):
        mini = min(A[i], B[j], C[k])
        maxi = max(A[i], B[j], C[k])
        diff = min(diff, maxi-mini)
        if A[i] == mini:
            i += 1
        elif B[j] == mini:
            j += 1
        else:
            k += 1
    return diff

A = [1, 4, 10]  
B = [2, 15, 20]  
C = [10, 12]
print(minimize(A, B, C))


# Method 2: decrease the max element
def minimize(A, B, C):
    i = len(A)-1
    j = len(B)-1
    k = len(C)-1
    diff = 10**9
    while i >= 0 and j >= 0 and k >= 0:
        mini = min(A[i],B[j],C[k])
        maxi = max(A[i],B[j],C[k])
        diff = min(diff, maxi - mini)
        if maxi is A[i]:
            i -= 1
        elif maxi is B[j]:
            j -= 1
        else:
            k -= 1
    return diff

print(minimize(A, B, C))
