# Given 3 sorted array A, B and C
# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

# Example: A = [1, 4, 10]  B = [2, 15, 20]  C = [10, 12]
# ans = 10 from A, 15 from B and 10 from C --> ans = 5

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