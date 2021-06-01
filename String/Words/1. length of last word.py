# Given a string, return the length of last word
# string = "Hello World ", return 5

# Logic: maintain the length of the current word
#   reset the length of word when next word begins, when whitespace encountered
#   Return the last length you have.

def solve(string):
    string = string.rstrip()
    count = 0
    
    if string == '':
        return 0

    for char in string:
        if char == " ":
            count = 0
        else:
            count += 1
    return count 

string = 'this is for testing purpose '
print(solve(string))

# Method 2: check the last word of string
def lengthOfLastWord2(string):
    count = 0
    if string == '':
        return 0
    for char in string[::-1]:
        if char == ' ':
            if count != 0:
                return count
        else:
            count += 1
    return count

print(lengthOfLastWord2(string))