# Given a number, find if it is colorful number or not
# colorful number: product of every digit of a sub-sequence are different
# Example: 234      {2} {3} {4} {2,3} {3,4}, product of each set is different
# 2-> 2    3-> 3    4-> 4    23-> 6    34-> 12 . Hence return True (1)


# Method 1: create sub-sequences of given number and check products of all sub-sequence
def colorful(number):
    number = str(number)
    n = len(number)

    # create the sub-sequences
    subSeq = []
    for i in range(n):
        for j in range(i,n):
            num = number[i:j+1]
            temp = list(map(int, num))
            subSeq.append(temp)
    
    # calculate product of each sub-sequences
    products = set()
    for sub in subSeq:
        p = 1
        for i in range(len(sub)):
            p *= sub[i]
        if p not in products:
            products.add(p)
        else:
            return 0
    return 1

num = 3245
print(colorful(num))


# Method 2: instead of creating sub-seq, we can directly calculate product of sub-seq
# 3245  ->  3  3*2  3*2*4  3*2*4*5
#           2  2*4  2*4*5
#           4  4*5
def colorful(num):
    num = list(str(num))
    product = set()
    n = len(num)
    for i in range(n):
        p = 1
        for j in range(i,n):
            p *= int(num[j])
            if p not in product:
                product.add(p)
            else:
                return 0
    return 1

print(colorful(num))
