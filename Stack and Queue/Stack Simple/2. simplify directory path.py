# Given a string A representing an absolute path for a file (Unix-style).
# Return the string A after simplifying the absolute path.

# Explanation:
# in unix '/' is root directory, '.' is current directory and '..' means
# we are moving back to parent directory
# Example: /a/b/../  --> we move from dir a to b and then '..' takes back
# from dir b to a

# Algorithm:
# split the expression about '/'
# for every element in splited_expr,
#     if ele is not '.' or '' or '..' --> append it in stack
#     elif ele is '..' then pop from stack
# after loop, return the directories with '/' in between them

def simplifyPath(string):
    expr = string.split("/")
    stack = []
    char = ['.', '..', '']
    for dir in expr:
        if dir not in char:
            stack.append(dir)
        
        # if dir is '..' and stack is not empty
        elif dir == '..' and stack:
            stack.pop()
    
    res = '/' + '/'.join(stack)
    return res

string = "/a/./b/../../c/"
print(simplifyPath(string))
