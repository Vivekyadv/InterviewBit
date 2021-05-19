# Given +ve integer n, return array having element from 1 to n
# but for multiple of 3, print "Fizz"
# for multiple of 5, print "Buzz"
# and for multiple of both 3 and 5, print "FizzBuzz"

def solve(n):
    ans = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans

print(solve(15))