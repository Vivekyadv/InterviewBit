# Given an array of real numbers greater than zero in form of strings.
# Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
# Return 1 for true or 0 for false.


def solve(A):
    # A is a list of strings
    n = len(A)
    arr = [float(i) for i in reversed(A)]
    sumi, x, y, z =  0.0, arr[0], arr[1], arr[2]
    for i in range(3, n):
        sumi = x + y + z
        if 1 < sumi < 2:
            return 1
        
        elif sumi > 2:
            # find max(x,y,z) and assign A[i] to it
            if x > y and x > z:
                x = arr[i]
            elif y > x and y > z:
                y = arr[i]
            else:
                z = arr[i]
        
        # when sumi < 1
        else:
            # find min(x,y,z) and assign A[i] to it
            if x < y and x < z:
                x = arr[i]
            elif y < x and y < z:
                y = arr[i]
            else:
                z = arr[i]
    
    sumi = x + y + z
    return int(1 < sumi < 2)

ar =  [ "2.673662", "0.573816", "2.454376", "0.403605", "0.806191" ]
print(solve(ar))
 