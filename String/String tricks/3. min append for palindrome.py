# Given a string, find the min characters to be appended to make the 
# string a palindrome

# Logic: iterate the given string
# find if string[i] == string[-1]
# if so, then check if string from i to end is palindrome of not

def isPalindrome(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return 0
        i += 1
        j -= 1
    return 1

def solve(string):
    i = 0
    j = len(string)-1
    count = 0

    while i < j:
        if string[i] == string[j]:
            # check if string[i:j] is palindrome
            # if string[i:j] == string[j:i:-1]:
            if isPalindrome(string, i, j):
                return count
        count += 1
        i += 1

    return count 

string = "abede"
print(solve(string))