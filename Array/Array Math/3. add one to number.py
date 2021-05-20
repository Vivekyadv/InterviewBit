# Given a number >= 0, represented as an array of digits, increment the number
# and return as array
# Example: num = [1,2,3,4] return [1,2,3,5]


# method 1: extract num from array --> add one --> return in form of array
def plusone(A):
    num = ''
    for el in A:
        num += str(el)
        
    addone = str(int(num) + 1)
    res = []
    for el in addone:
        res.append(int(el))
        
    return res


# method 2: iterate array from the end --> res = arr[i] + 1 and check 
# if res < 10: --> then store the res in arr[i] and break the loop
# else: store res % 10 in arr[i] and pass the carry to next iteration

# end case: [9,9,9] :: at the end of loop, carry will be 1 ans arr = [0,0,0]
# add arr = carry + arr 


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