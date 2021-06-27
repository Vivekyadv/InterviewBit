# Find the number of distinct Max Heap can be made from A distinct integers.

# Example: A = 4
#  Let us take 1, 2, 3, 4 as our 4 distinct integers
#  Following are the 3 possible max heaps from these 4 numbers :
#       4           4                     4
#     /  \         / \                   / \ 
#    3    2   ,   2   3      and        3   1
#   /            /                     /

#  1            1                     2 


mod = 10**9 + 7
def comb(r,n) :
    if 2*r > n : 
        return comb(n-r,n)
    c = 1
    for i in range(r) :
        c = c*(n-i)//(i+1)
    return c

def solve(self, A):
    mod = pow(10,9) + 7
    ans,h = [1,1], 0
    for n in range(2,A+1) :
        if 2<<h <= n :
            h += 1
        m = n-(1<<h)+1
        l = (1<<(h-1))-1 + min(m,1<<(h-1))
        r = (1<<(h-1))-1 + max(0,m-(1<<(h-1)))
        ans.append((comb(l,n-1)*ans[l]*ans[r])%mod)
    return ans[A]