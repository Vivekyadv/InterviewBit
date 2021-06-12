# Given a string which consists only '(' and ')'
# find whether parantheses in A is balanced or not 
# if it is balanced then return 1 else return 0

def solve(expr):
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        else:
            # if it is ')' closing bracket then stack can't be empty
            if not stack:
                return 0
            pop_char = stack.pop()
            if pop_char == '(' and char != ')':
                return 0
    return 1 if stack else 0

print(solve("((()))"))
