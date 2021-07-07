# Given an integer array consisting of unique elements from 1 to n. you can swap any two 
# integers at most B times. Return the largest lexicographical value array that can be 
# created by executing atmost B swaps.

# arr = 8 2 7 4 5 6 3 1 ,   B = 2
# 1st swap -> (2,7) -> 8 7 2 4 5 6 3 1
# 2nd swap -> (2,6) -> 8 7 6 4 5 2 3 1


def solve(arr, B):
    n = len(arr)
    pos = {}

    for i in range(n):
        pos[arr[i]] = i

    for i in range(n):
        if B == 0:
            break
        if arr[i] != n:
            temp = arr[i]
            arr[i] = n
            arr[pos[arr[i]]] = temp
            pos[temp] = pos[arr[i]]
            B -= 1
        n -= 1

    return arr

arr = [ 10, 9, 8, 7, 6, 4, 5, 2, 1, 3 ]
print(solve(arr, 3))  


def solve(arr, B):
    dic = {}
    count = 0
    n = len(arr)
    
    for i in range(n):
        
        key = arr[i]
        while key in dic:
            arr[i] = dic[key]
            new_key = dic[key]
            del dic[key]
            key = new_key
        
        if count < B and arr[i] != n - i:
            dic[n - i] = arr[i]
            count += 1
            arr[i] = n - i
                
    return arr

arr = [ 8, 2, 7, 4, 5, 6, 3, 1 ]
print(solve(arr, 2))