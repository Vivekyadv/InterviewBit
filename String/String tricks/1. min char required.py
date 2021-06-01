# Given an string A. The only operation allowed is to insert char
# in the beginning of the string. Find how many min char are need 
# to be inserted to make the string a palindrome string.

# Logic: iterate the string and check 
# reverse[:i] + string == reverse + string[-i:]
# if so then, return the index


def solve(string):
    reverse = string[::-1]
    if reverse == string:
        return 0
    for i in range(1, len(reverse)):
        if reverse[:i] + string == reverse + string[-i:]:
            break
    return i

string = "AACECAAAA"
print(solve(string))

# Method 2: use KMP algorithm

def computeLPS(string):
    n = len(string)
    lps = [None] * n
    length = 0
    lps[0] = 0
    i = 1
    while i < n:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def solve(string):
    if len(string) <= 1:
        return 0
        
    revStr = string[::-1]
    concat = string + "$" + revStr
    lps = computeLPS(concat)
    
    return len(string) - lps[-1]
    
string = "hqghumeaylnlfdxfi"
print(solve(string))