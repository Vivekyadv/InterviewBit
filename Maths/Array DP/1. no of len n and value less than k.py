# given set of digits in sorted order, find how many numbers of 
# length B whose value is < number C

MAX = 10

def numInarr(N):
    digit = []
    num = str(N)
    for i in range(len(num)):
        digit.append(int(num[i]))
    return digit


def solve(A, B, C):
    d2 = 0

    digit = numInarr(C)
    len_A = len(A)

    # Case 1: when B > len(C) --> no possible solution
    if B > len(digit) or len_A == 0:
        return 0

    # Case 2: when B < len(C)
    elif B < len(digit):
        # base case ::: 012, 01 is 12 and 1 ie starting with 0's
        if A[0] == 0 and B != 1:
            return (len_A - 1) * pow(len_A, B - 1)
        else:
            return pow(len_A, B)

    # Case 3: when B == len(C)
    else:
        dp = [0 for i in range(B + 1)]
        lower = [0 for i in range(MAX + 1)]

        for i in range(len_A):
            lower[A[i] + 1] = 1
        for i in range(1, MAX + 1):
            lower[i] = lower[i - 1] + lower[i]

        flag = True
        dp[0] = 0
        for i in range(1, B + 1):
            d2 = lower[digit[i - 1]]
            dp[i] = dp[i - 1] * len_A


            if (i == 1 and A[0] == 0 and B != 1):
                d2 = d2 - 1

            if (flag):
                dp[i] += d2

            flag = (flag & (lower[digit[i - 1] + 1] == lower[digit[i - 1]] + 1))

        return dp[B]

A = [0,1,2,3,4]
B = 2               
C = 23

print(solve(A,B,C))