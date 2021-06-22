# Given three arrays A,B,C. return list of numbers which is present in at least 2 out of 3
# arrays, list should be sorted.

# Method 1: for elements in A, store ele which is present in other arrays (either in B or C)
# similarly for B and C, store ele present in other arrays

def solve(A, B, C):
    res = []
    for ele in A:
        if ele in B or ele in C:
            res.append(ele)
    
    for ele in B:
        if ele in A or ele in C:
            res.append(ele)
    
    for ele in C:
        if ele in A or ele in B:
            res.append(ele)
            
    res = list(set(res))
    res.sort()
    return res


# Method 2: using set.intersection
# Take intersection of A, B, C
def solve(A, B, C):
    A_B = set(A).intersection(set(B))
    B_C = set(B).intersection(set(C))
    A_C = set(A).intersection(set(C))

    intersec = A_B.union(B_C).union(A_C)
    result = list(intersec)
    result.sort()
    return result


# Method 3: using hash table. count perticular ele in all 3 arrays and then store those ele
# whose count >= 2. return ans in sorted form
def updateTable(hashTable, arr):
    for ele in set(arr):
        if ele in hashTable:
            hashTable[ele] += 1
        else:
            hashTable[ele] = 1

def solve(A, B, C):
    hashTable = {}
    updateTable(hashTable, A)
    updateTable(hashTable, B)
    updateTable(hashTable, C)

    # now store ele having count >= 2
    result = []
    for ele in hashTable:
        if hashTable[ele] >= 2:
            result.append(ele)
    
    result.sort()
    return result

A = [1,1,2,3]
B = [2,3,5,4]
C = [3,5,6]
print(solve(A, B, C))
