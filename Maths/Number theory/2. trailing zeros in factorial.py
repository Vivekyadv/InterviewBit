# Given an integer n, return number of trailing zeroes in n!
# Hint: no of 2' is always < no of 5's in n!, hence count no of 5's
# no of 5's = num//5 + num//5^2 + num//5^3 ...

def solve(num):
    res = 0
    i = 1
    rem = num
    while rem > 0:
        rem = num//pow(5,i)
        res += rem
        i += 1
    
    return res
    
print(solve(120))
