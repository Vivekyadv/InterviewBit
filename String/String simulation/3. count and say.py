# count and say number ::: 
# Example 111221 --> three 1's, two 2's, one 1 --> ans = 312211

def countAndSay(num):
    if num == 1:
        return '1'
    if num == 2:
        return '11'
    result = '11'
    for i in range(3, num+1):
        temp = ''
        result += '@'
        count = 1
        for j in range(len(result)-1):
            if result[j] == result[j+1]:
                count += 1
            else:
                temp += str(count)
                temp += result[j]
                count = 1
        result = temp
    return result

print(countAndSay(6))
