# Given integer n, generate square matrix with element 1 to n^2
# in spiral order

# Algorithm: maintain top, bottom, left and right ::: count = 1
#            iterate, increment and store value of count
# step 1: iterate top in range(left,right+1)
#         top ++
# step 2: iterate right in range(top,bottom+1)
#         right --
# step 3: iterate bottom in range(right,left-1,-1)
#         bottom --
# step 4: iterate left in range(bottom,top-1,-1)
#         left ++


def solve(n):
    top = left = 0
    bottom = right = n-1
    count = 1
    matrix = [ [0 for i in range(n)] for j in range(n)]
    while top <= bottom and left <= right:
        for j in range(left,right+1):
            matrix[top][j] = count
            count += 1
        top += 1

        for i in range(top,bottom+1):
            matrix[i][right] = count
            count += 1
        right -= 1

        for j in range(right,left-1,-1):
            matrix[bottom][j] = count
            count += 1
        bottom -= 1

        for i in range(bottom, top-1,-1):
            matrix[i][left] = count
            count += 1
        left += 1

    return matrix

print(solve(3))



