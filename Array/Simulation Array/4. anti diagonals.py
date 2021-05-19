# Given a NxN matrix, return anti diagonals of it
# 1 2 3             
# 4 5 6         anti diagonals: 1, 2-4, 3-5-7, 6-8, 9
# 7 8 9

# Algorithm:
#   00 01 02
#   10 11 12    anti-diagonal: [00], [01,10], [02,11,20], [12,21], [22]
#   20 21 22              i+j:   0      1          2         3       4
#
#   store those element having index (i+j)
#


def diagonal(A):
    n=len(A)
    ans=[[] for i in range(2*n-1)]
    for i in range(n):
        for j in range(n):
            ans[i+j].append(A[i][j])
    return ans

arr = [
    [11,12,13,14],
    [15,16,17,18],
    [19,20,21,22],
    [23,24,25,26]
]

print(diagonal(arr))


def solve2(A):
    n = len(A)
    ans = []

    for i in range(n):
        temp = []
        row = 0
        colm = i
        while row < n and colm >= 0:
            temp.append(A[row][colm])
            row += 1
            colm -= 1
        ans.append(temp)

    for i in range(1,n):
        temp = []
        row = i
        colm = n-1
        while row < n and colm >= 0:
            temp.append(A[row][colm])
            row += 1
            colm -= 1
        ans.append(temp)
    return ans

print(solve2(arr))
