# Given array of strings, find longest string S which is prifix of all strings in array

# Algorithm: Find smallest and largest string in array and using loop, check the prifix

def longestCommonPrefix(arr):
    word1 = min(arr)
    word2 = max(arr)
    indx = 0
    n = min(len(word1), len(word2))
    for i in range(n):
        if word1[i] == word2[i]:
            indx += 1
    return word1[:indx]