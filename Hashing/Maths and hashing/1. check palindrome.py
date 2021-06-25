# Given a string consisting lowercase letters. check if letters can be rearranged to 
# form a palindrome. return 1 if rearrangement is possible else 0

def solve(string):
    table = {}
    for char in string:
        if char == ' ':
            continue
        if char in table:
            table[char] = table[char]%2 + 1
        else:
            table[char] = 1

    odd = 0
    for i in table:
        if table[i] & 1:
            odd += 1

    if odd <= 1:
        return 1
    else:
        return 0

string = 'this is thi'
print(solve(string))

# Approach 2: traverse the string, if char is present in table, remove it from table
# if not present then add in table. after the loop, if len(string) is odd then 
# table must have only one element, if len even then table must have 0 element

def solve(string):
    table = []
    for char in string:
        if char in table:
            table.remove(char)
        else:
            table.append(char)

    n = len(string) % 2
    m = len(table)

    if n == m:
        return 1
    else:
        return 0

print(solve(string))


# Approach 3: using bitwise XOR
# for char in string, convert in numbers then take XOR of all numbers
# XOR of similar values = 0, after the loop we have either XOR = 0 (if all char 
# appears even number of time) or a single char 

# Note: for single character, we take (num & num-1) which given 0

def solve(string):
    xor = 0
    for str in string:
        xor ^= 1 << ord(str)
    
    if xor == 0 or xor & (xor-1) == 0:
        return 1
    else:
        return 0

print(solve(string))
