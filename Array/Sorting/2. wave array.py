# sort the given array into a wave like array and return it,
# In other words, arrange the elements into a sequence 
# such that a1 >= a2 <= a3 >= a4 <= a5.....

# Algorithm:
# step 1: sort array
# step 2: swap adjacent element under loop with inc = 2


def arrange(A):
    n = len(A)
    A.sort()
    for i in range(0, n-1, 2):
        A[i], A[i+1] = A[i+1], A[i]
    return A

print(arrange([4,5,7,3,5,2]))