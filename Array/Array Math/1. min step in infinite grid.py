# You are in an infinite 2D grid where you can move in any of the 8 directions 
# left, right, up, down, (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
# you are given a sequence of points and the order in which you need to cover 
# the points.. Give the minimum number of steps in which you can achieve it. 
# You start from the first point.

def coverPoints(A, B):
    steps = 0
    for i in range(len(A) - 1):
        distance = max(abs(A[i+1]-A[i]), abs(B[i+1]-B[i]))
        steps += distance
    
    return steps

a = [1,4]
b = [3,5]
print(coverPoints(a,b))

# (1,3) to (4,5) ::: 4-1 steps in x direction and 5-3 steps in y direction,
# we have to take maximum of it. 