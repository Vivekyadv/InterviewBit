# find pascale triangle till nth row
# n = 4
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

def getRow(k):
    ans = []
    prev = 1
    for i in range(k+1):
        curr = prev * (k-i) // (i+1)
        ans.append(prev)
        prev = curr
    return ans

def solution(n):
    result = []
    for i in range(n):
        result.append(getRow(i))
    
    return result

print(solution(5))


# using ith element of row = (i-1)th element of previous row 
#                            + ith element of previous row

def generate(A):
    if A <= 0:
        return []
    result = [[1]]
    for r in range(1, A):
        row = [1]
        for i in range(1,r):
            row.append(result[r-1][i-1] + result[r-1][i])
        row.append(1)
        result.append(row)
    return result

print(generate(5))