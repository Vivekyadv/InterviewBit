# given array which contains 0 & 1 and a number k, find the len of
# longest subsegment of 1's possible by changing at most k '0's

# Method: use two pointer algo
# maintain subarray from i to j such that no_of_0s <= k
# if no_of_0s > k, then increment i
# at every step, check max size (j-i+1)
def longestSubSeg(arr, k):
    count0 = 0
    i = 0
    max_size = 0

    for j in range(len(arr)):
        if arr[j] == 0:
            count0 += 1

        while count0 > k:
            if arr[i] == 0:
                count0 -= 1
            i += 1

        size = j - i + 1
        max_size = max(max_size, size)
    return max_size

arr = [1, 0, 0, 1, 0, 1, 0, 1 ]
k = 2
print(longestSubSeg(arr, k))
