# Given a matrix, A of size M x N of 0s and 1s. 
# If an element is 0, set its entire row and column to 0.

def setZeros(A):
    # M x N :::: M- rows and N- columns
    m = len(A)
    n = len(A[0])

    indxi, indxj = set(), set()
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                indxi.add(i)
                indxj.add(j)

    for i in indxi:
        for j in range(n):
            A[i][j] = 0
    
    for j in indxj:
        for i in range(m):
            A[i][j] = 0
    
    return A

arr =[
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 1]]
print(setZeros(arr))
