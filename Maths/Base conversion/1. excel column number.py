# Given a column title A as appears in an Excel sheet, return its corresponding column number.
# ABC --> a*pow(26,2) + b*pow(26,1) + c*pow(26,0)  
# a,b,c are indx of alphabets (1,2,3...26)


def titleToNumber(title):
    result = 0
    n = len(title)
    for i in range(n):
        indx = ord(title[i]) - ord('A') + 1
        result += indx * pow(26, n-i-1)

    return result

print(titleToNumber('AAH'))

# method 2
def title2Number(title):
    result = 0
    for i in range(len(title)):
        indx = ord(title[i]) - ord('A') + 1
        result = result*26 + indx

    return result

print(title2Number("AAH"))