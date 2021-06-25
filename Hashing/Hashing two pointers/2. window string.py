# Given two strings S and T. find the min window in S which will contain all characters
# of T. solve it in O(n) Time
# 
# Example:  S = 'ADOBECODEBANK'   T = 'ABC'   min window = 'BANK' 


from collections import defaultdict
def findSubString(string, pat):
    strLen = len(string)
    patLen = len(pat)

    if strLen < patLen:
        # No such window exists 
        return ''

    map2 = defaultdict(lambda: 0)
    map1 = defaultdict(lambda: 0)

    for i in range(patLen):
        char = pat[i]
        map2[char] += 1

    i, min_len = 0, float('inf')
    start = -1

    count = 0 # count of characters
    for j in range(strLen):
        char = string[j]
        map1[char] += 1

        if map1[char] <= map2[char]:
            count += 1

        # if all the characters are matched
        if count == patLen:

            # Try to minimize the window
            # while frequency of char in map1 > freq of char in map2 or the char is not
            # mendatory char. we'll decrement the freq of char in map1
            while map1[string[i]] > map2[string[i]] or map2[string[i]] == 0:

                if map1[string[i]] > map2[string[i]]:
                    map1[string[i]] -= 1

                i += 1

            # update window size
            windowLen = j - i + 1
            if min_len > windowLen:
                min_len = windowLen
                start = i

    return string[start: start + min_len] if min_len != float('inf') else ''


s = 'adobecodebanc'
t = 'abc'
print(findSubString(s,t))


def solve(string, pat):
    table = {}
    num_uniq = len(set(pat))
    for char in pat:
        if char in table:
            table[char] -= 1
        else:
            table[char] = 0
    
    count_uniq = 0
    
    head = 0
    tail = 0
    ret = ""
    
    while (True):
        if count_uniq < num_uniq:
            # advance head
            if head == len(string):
                break
            char = string[head]
            if char in table:
                if table[char] == 0:
                    count_uniq += 1
                table[char] += 1
            head += 1
        else:
            # check if tail:head substring is shorter than existing solution
            if ret == "":
                ret = string[tail:head]
            else:
                if len(ret) > (head-tail):
                    ret = string[tail:head]
            # advance tail
            
            char = string[tail]
            if char in table:
                if table[char] == 1:
                    count_uniq -= 1
                table[char] -= 1
            tail += 1
    

    return ret

print(solve(s, t))