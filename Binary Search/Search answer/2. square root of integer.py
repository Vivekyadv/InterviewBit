# given an int, calculate square root of it. If num is not 
# perfect square, then return floor value 

def sqrt(num):
    if num in [0,1]:
        return num
    start, end = 0, num
    while start <= end:
        mid = (start + end )//2
        if mid**2 == num:
            return mid
        elif mid**2 < num:
            start = mid+1
            ans = mid
        elif mid**2 > num:
            end = mid-1
    return ans

print(sqrt(125))
