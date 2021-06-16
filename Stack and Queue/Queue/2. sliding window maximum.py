def slidingMaximum(A, B):
    q = []
    result = []
    for i in range(len(A)):
        q.append(A[i])
        if i>0 and q and q[0]==A[i-B]:
            q.pop(0)
        ind=0
        while q and ind<len(q):
            if q[ind]<A[i]:
                q.pop(ind)
            else:
                ind+=1
        if i+1>=B:
            result.append(q[0])
            
    return result

A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print(slidingMaximum(A, B))