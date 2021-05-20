# given set of digits in sorted order, find how many numbers of 
# length B whose value is < number C

# Example:
    # A = {0,1,2,5}
    # B = 2                     # output: 5 {10,11,12,15,20}
    # C = 21

# Case 1: B > len(C) --> no solutions
# A = {0,1,4,8}
# B = 3               there is no 3 digit number less than 59
# C = 59

# Case 2: B < len(C)
# A = {0,1,4,8}
# B = 3           
# C = 2373

# if 0 not in A:
#     _ _ _ = 4*4*4   --> pow(len(A), B)    len(A) = 4 
# else:
#     if B == 1:
#         pow(len(A), B)
#     _ _ _ = 3*4*4   --> (len(A)-1) * pow(len(A)-1, B-1)

# Case 3: B = len(C)
# A = {0,1,2,3,4}
# B = 2               [10,11,12,13,14,20,21,22,23,24,30,...]
# C = 23

# Extract number starting with 2 (first digit of C) and then exclude num > C