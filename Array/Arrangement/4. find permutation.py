# Given +ve int n and a string s consisting of letters D or I, 
# you have to find any permutation of first n positive integer that 
# satisfy the given input string.

# D means next number is smaller, while I means next number is greater.

# Notes

# Length of given string s will always equal to n - 1
# Your solution should run in linear time and space.


def findperm(s,n):
    res = []
    inc = 1
    dec = n
    for x in s:
        if x == 'I':
            res += [inc]
            inc += 1
        elif x == 'D':
            res += [dec]
            dec -= 1
    res += [inc if s[-1] == 'I' else dec]
    return res


string = 'IDDDI'
num = len(string) + 1
print(findperm(string, num))