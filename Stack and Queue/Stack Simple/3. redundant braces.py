# Given a string A denoting an expression. It contains the following operators 
# ’+’, ‘-‘, ‘*’, ‘/’. Return 1 if A has redundant braces, else return 0.
# Note: A will be always a valid expression. Ex: ((a + b))

# Logic: there must be at least one operator in ()
# we'll move till we find closing brac ')'
#     then till '(' we'll pop element (including operators and operands) 
#     if there is no operator in () then it is redundant 

def braces(string):
    stack = []
    for char in string:
        # if char is '(' or operator or variable --> push in stack
        if char != ')':
            stack.append(char)

        else:
            # if it is closing braces, pop from stack and redund = True
            top = stack.pop()
            redund = True

            # now pop every in element between (), and if we found any 
            # operator in between (), then parand = False
            while top != '(':
                if top in '+-*/':
                    redund = False
                top = stack.pop()
                
            if redund:
                return 1
    return 0 

string = "((a+b))"
print(braces(string))

# Logic 2: there must be at least 2 element in (), 
# if no_of_ele is <= 1   ::  it is redundant

def braces(string):
    stack = []
    
    for char in string:
        if char != ')':
            stack.append(char)
        else:
            top = stack.pop()
            count = 0

            while top != '(':
                count += 1
                top = stack.pop()
            
            if count <= 1:
                return 1
    return 0

print(braces(string))
