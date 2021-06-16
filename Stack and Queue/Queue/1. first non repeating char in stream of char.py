# Given string of char, only lowercase char. make another string B which is
# formed such that we have to find first non repeating char each time a char is
# inserted. if non repeating char is found, append #
# Example: ababc
    # "a"      -   first non repeating character 'a'
    # "ab"     -   first non repeating character 'a'
    # "aba"    -   first non repeating character 'b'
    # "abab"   -   first non repeating character '#'
    # "ababc"  -   first non repeating character 'c'


# Algorithm: iterate each characters in given string
# if char is not visited, then add in queue and mark it visited
# if char is visited then remove from queue (make sure to not remove repeated 
# char which is already remvoed)
# first non repeating char will be front of queue, i.e. queue[0]
# if queue is not empty ans += queue[0], else '#'

def solve(string):
    queue = []
    visited = set()
    ans = ''
    for char in string:
        # if char is not visited, add in queue and mark it visited
        if char not in visited:
            queue.append(char)
            visited.add(char)
        else:
            # if char is visited, that means it is repeated char, remove from queue 
            # but make sure to not remove repeated char which is already removed
            if char in queue:
                queue.remove(char)
        
        letter = queue[0] if queue else '#'
        ans += letter
    return ans

string = 'hszrqozqrr'
print(solve(string))
print(solve('ababc'))
