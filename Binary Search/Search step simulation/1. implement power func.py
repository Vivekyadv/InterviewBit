# Implement pow(x, n) % d.

def power(x,n,d):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * x
            res = res % d
        n = n//2
        x = (x * x) % d
    res = res % d
    return res

print(power(5,7,7))



# pow(x,n) func ::: just for concept
# def pow(x,n):
#     if n == 0:
#         return 1
#     res = 1
#     while n > 0:
#         if n % 2 == 1:
#             res = res*x
#             n -= 1
#         else:
#             x = x*x
#             n = n//2
#     return res
# print(pow(3,8))