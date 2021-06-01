# Given a string A. Return the string A after reversing the string word by word

# Example:
#     A = "the sky is blue" --> ans = "blue is sky the"
#     A = "this is ib"      --> ans = "ib is this"


def solve(string):
    string = string.split()
    string.reverse()
    return ' '.join(string)