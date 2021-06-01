# given a string, check if it is a palindrome, consider only alpha-numeric and ignore cases
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Method 1: store only alpha numeric and check it's reversed string
def solve(string):
    st = ''
    for el in string:
        if el.isalnum():
            st += el
    st = st.lower()
    return int(st == st[::-1])

string = "'A man, a plan, a canal: Panama'"
print(solve(string))

# Method 2: solve this using 2 pointers
def solve(string):
    i = 0
    j = len(string)-1
    while i <= j:
        if string[i].isalnum() and string[j].isalnum():
            si = string[i].lower()
            sj = string[j].lower()
            if si != sj:
                return 0
            else:
                i += 1
                j -= 1
        elif not string[i].isalnum():
            i += 1
        elif not string[j].isalnum():
            j -= 1
    return 1

print(solve(string))
