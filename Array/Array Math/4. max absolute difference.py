def maxArr(A):
    a, b = [], []
    for i in range(len(A)):
        a.append(A[i] + i)
        b.append(A[i] - i)
    result = max(max(a)-min(a), max(b)-min(b))
    return result

print(maxArr([1,3,-1]))
