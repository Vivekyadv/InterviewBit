# Given a string s, find the no of amazing substrings of s
# Amazing substrings are those which start with a vowel

# Example: string = ABEC
# Amazing Substrings --> A, AB, ABE, ABEC, E, EC

# Logic: iterate string ::: 
# if string[i] is vowel then count no of characters from that vowel
# to end of string. Those are the no of amazing substrings start 
# with string[i]

def solve(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() in 'aeiou':
            count += (len(string)-i)
    return count % 10003

print(solve("ABEC"))