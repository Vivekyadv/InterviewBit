# Determine whether an integer is a palindrome. Do this without extra space.
# method 1: convert into string and reverse it ::: space = O(n)

def solve1(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else: 
        return False

# method 2: reverse the number:: divide it by 10 and store remainder

def solve2(num):
    rev = 0
    n = num
    while n > 0:
        rev = rev*10 + n %10
        n = n//10
    
    return rev == num

print(solve1(2147447412))
print(solve2(2147447412))