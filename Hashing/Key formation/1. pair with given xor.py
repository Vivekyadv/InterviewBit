# Given an array which contain distinct integers. find the no of unique pairs of 
# integers in array whose XOR is B

def solve(arr, val):
    table = set()
    count = 0
    for ele in arr:
        if val ^ ele in table:
            count += 1
        else:
            table.add(ele)
    return count

arr = [3, 6, 8, 10, 15, 50]
val = 5
print(solve(arr, val))


def solve(arr, val):
    count = 0
    table = {}
    for ele in arr:
        table[ele] = 1
    
    for ele in arr:
        xor = ele ^ val
        if xor in table:
            count += 1
    
    return count//2    

print(solve(arr, val))