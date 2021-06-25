# Given a string, find the length of longest substring without repeating characters

# Approach: using two pointers (i,j) 
# inc j if char is not seen, and calculate length (j-i)
# if char is seen, then inc i and remove char from seen

def solve(string):
    n = len(string)
    i = j = 0
    max_len = 0
    store = set()
    while i < n and j < n:
        char = string[j]
        if char not in store:
            store.add(char)
            j += 1
            max_len = max(max_len, j-i)
        else:
            store.remove(char)
            i += 1
            
    return max_len

string = 'abbacbcdbadb'
print(solve(string))

# Approach:
# store the index of seen characters and use sliding window to calculate lenght 
# i -> starting index       j -> ending index
# scan from left to right and keep track of max length
# if current char is already seen, increment i. if not then inc j
def solve(A):
    i = 0
    max_len = 0
    store = {}
    for j in range(len(A)):
        char = A[j]
        if char in store and store[char] >= i:
            max_len = max(max_len, j - i)
            i = store[char] + 1
        store[char] = j
    return max(max_len, j - i + 1)

print(solve(string))
