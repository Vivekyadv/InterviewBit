# Given expression, evaluate and return its value
# Example: '5'   '3'   '+'   '4'   '-'   '10'   '2'   '/'   '*'
# (((5+3) - 4) * (10/2))   --> (8)- 4) * (5) --> 20

def evaluate(expr):
    stack = []
    for char in expr:
        if char not in '+-*/':
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(b+a)
            elif char == '-':
                stack.append(b-a)
            elif char == '*':
                stack.append(b*a)
            else:
                stack.append(b//a)
    return stack[0]

expr = ['5', '3', '+', '4', '-', '10', '2', '/', '*']
print(evaluate(expr))