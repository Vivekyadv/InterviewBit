def plusone(A):
    num = ''
    for el in A:
        num += str(el)
        
    addone = str(int(num) + 1)
    res = []
    for el in addone:
        res.append(int(el))
        
    return res

def plusOne(A):
    val = 1
    for i in range(len(A)-1,-1,-1):
        val += A[i]
        carry = val // 10
        if carry == 0:
            A[i] = val
            break
        else:
            A[i] = val % 10
            val = carry
    A = [carry] + A
    while A[0] == 0:
        del A[0]
    return A

print(plusOne([1,2,3,4,5]))
print(plusone([9,9,9,9]))