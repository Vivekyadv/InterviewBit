# Given a string, find the rank of the string amongst its 
# permutations sorted lexicographically.

# find rank of bca: ans = 4
# The order permutations with letters 'a', 'c', and 'b' : 
# abc --> acb --> bac --> bca --> cab --> cba

def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    f = 1
    while n > 1:
        f = f*n
        n -= 1
    return f

def solve(word):
    rank = 0
    for i in range(len(word)):
        count = 0
        num = fact(len(word) - (i+1))
        for j in range(i+1, len(word)):
            if word[i] > word[j]:
                count += 1
        rank += count*num
    return (rank+1)

print(solve('ibytes'))


# method 2: 
def findRank(A):
    A = list(A)
    chars = A[:]
    chars.sort()
    rank = i =0
    while i < len(A):
        indx = chars.index(A[i])
        if indx != 0: 
            rank += fact(len(A)-i-1)*indx
        else:
            if chars == A:
                break
        chars.pop(indx)
        A.pop(i)
    return rank+1

print(findRank('aebcd'))
print(findRank('ibytes'))
