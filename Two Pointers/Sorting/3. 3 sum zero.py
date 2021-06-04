# Given array, find all triplet with sum = 0

def solve(arr):
    arr.sort()
    n = arr.__len__()
    ans = []
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            add = arr[i] + arr[j] + arr[k]
            pair = [arr[i], arr[j], arr[k]]
            if add < 0:
                j += 1
            elif add > 0:
                k -= 1
            else:
                ans.append(pair)
                while j < k and arr[j+1] == arr[j]:
                    j += 1
                j += 1
                while j < k and arr[k-1] == arr[k]:
                    k -= 1
                k -= 1

    return ans

arr = [-3, -3, -3, -3, -3, -1, -1, -1, -1, 0, 1, 2]
print(solve(arr))
