# Given 4 numbers, check if a rectangle can be formed 
# using those numbers
#
# possibilities for rectangle:  
#            a = b and c = d
#            a = c and b = d
#            a = d and c = b

def solve(a,b,c,d):
    if (a == b and c == d) or (a == c and b == d) or (a == d and c == b):
        return True
    return False

print(solve(12,45,12,45))

def solve2(a,b,c,d):
    arr = [a,b,c,d]
    arr.sort()

    if arr[0] == arr[1] and arr[2] == arr[3]:
        return True
    return False

print(solve2(1,1,4,4))
