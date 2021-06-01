# Given two strings, A and B, find the index of B if B is in A
# Logic: iterate through string A
# check if string B == to string A from i to len(B)

def solve(str_A, str_B):
    n = len(str_B)
    for i in range(len(str_A)):
        if str_A[i:i+n] == str_B:
            return i
    return -1

a = 'thisisfortestingyouhavetowait'
b = 'test'
print(solve(a,b))