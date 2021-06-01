# Implement atoi to convert a string to an integer.

def atoi(self, A):
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    b = A.strip('$' '%' '#' '!' '@' '%' '^' '&' '*' '(' '_' ')' '+' "/" "?" '>' 
    '<' '.' ';' ':').split(' ')
    
    box = []
    for i,char in enumerate(b[0]):
        if char.isalpha():
            box.append(i)
        if len(box)!=0:
            b[0] = b[0][:box[0]]
    
    try : z = int(b[0])
    except: z=0
    return  max(MIN_INT , min(z, MAX_INT))