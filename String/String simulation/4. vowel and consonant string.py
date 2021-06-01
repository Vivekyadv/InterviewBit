# Given a string, find no of substring which starts with vowels and end with 
# consonants or vice versa:
# return the count modulo 1000000007


def solve(string):
    mod = 1000000007
    n = len(string)
    count = 0
    if len(string) == 0 or len(string) == 1:
        return 0
    vow=[0]*n
    con=[0]*n
    
    for i in range(n-2,-1,-1):
        if string[i+1] in "aeiou": 
            vow[i] += 1
        else:
            con[i] += 1
    for i in range(n-2,-1,-1):
        vow[i] += vow[i+1]
        con[i] += con[i+1]
        
    for i in range(n-1):
        if string[i] in "aeiou": 
            count += con[i]
        else:
            count += vow[i]
            
    return count % mod

string = "abacb"
print(solve(string))