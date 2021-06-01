# validate if a given string is numeric
# Examples: 
#   "0"     => true
#   " 0.1 " => true
#   "abc"   => false
#   "1 a"   => false
#   "2e10"  => true

def isNumber(num):
    try:
        x = float(num)
        y = num.split('e')
        for ele in y:
            if ele == "":
                return 0
            if ele[-1] == ".":
                return 0
        return 1
    except:
        return 0

num = ['0' , '3.', '13e-1', '81e5', '23+7', '0.03e0.2', '012']
for n in num:
    print(isNumber(n), n)
