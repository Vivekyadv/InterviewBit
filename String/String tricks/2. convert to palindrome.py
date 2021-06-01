# Given a string, check whether it is possible to make this string a 
# palindrome after removing exactly one character


def solve(string):
    if string == string[::-1]:
        return 1
    i = 0
    j = len(string)-1
    
    while i <= j:
        if string[i] != string[j]:
            str1 = string[:i] + string[i+1:]
            str2 = string[:j] + string[j+1:]
            if str1 == str1[::-1] or str2 == str2[::-1]:
                return 1
            else:
                return 0
                
        i += 1
        j -= 1
    
string = "thisfsiht"
print(solve(string))
