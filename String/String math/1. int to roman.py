# Given a number, convert it into roman number and return in the form of string

def intToRoman(num):
    val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    res = ''
    i = len(val)-1
    while num:
        for x in range(num//val[i]):
            res += roman[i]
        num = num % val[i]
        i -= 1
    return res

print(intToRoman(49))


# def solve(num):
#     res = ""
#     val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#     i = 0
#     while num > 0:
#         for x in range(num//val[i]):
#             res += roman[i]
#         num = num % val[i]
#         i += 1
#     return res

# print(solve(38))
