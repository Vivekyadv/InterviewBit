# Given n points on a 2D plane, find the maximum no of points that lie on the same straight
# line. You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])


# Editorial solution
def maxPoints(A, B):
    maxi = 0
    if len(A) < 2:
        return len(A)
    for i in range(len(A)-1):
        mapper = {}
        repeated_points = 0
        for j in range(i+1, len(A)):
            if A[j] != A[i]:
                x_diff = A[j] - A[i]
                y_diff = B[j] - B[i]
                slope = float(y_diff)/float(x_diff)
            elif B[j] == B[i]:
                repeated_points +=1
                continue
            else:
                slope = "undefined"
            
            if mapper.get(slope):
                mapper[slope]+=1
            else:
                mapper[slope] = 1

        for key,value in mapper.items():
            maxi = max(maxi,value+repeated_points)
        if len(mapper) == 0:
            maxi = max(maxi,repeated_points)

    return maxi+1

a = [-1, 0, 1, 2, 3, 3]
b = [ 1, 0, 1, 2, 3, 4]
print(maxPoints(a,b))