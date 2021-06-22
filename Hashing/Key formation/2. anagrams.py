# Given an array of strings, return all groups of strings that are anagrams. 
# Represent a group by a list of integers representing the index in the original list.

# Example: Input : [cat, dog, god, tca]   Output : [[1, 4], [2, 3]]

def anagrams(arr):
    table = {}

    for i in range(len(arr)):
        sortStr = ''.join(sorted(arr[i])) 
        if sortStr not in table:
            table[sortStr] = [i+1]
        else:
            table[sortStr].append(i+1)
            
    return list(table.values())

arr = ['tea', 'cat', 'dog', 'word', 'god', 'eat', 'tca']
print(anagrams(arr))


def anagrams(arr):
    arr = list(arr)
    for i in range(len(arr)):
        sortStr = sorted(arr[i])
        arr[i] = ''.join(sortStr)

    table = {}
    
    for i in range(len(arr)):
        if arr[i] not in table:
            table[arr[i]] = [i+1]
        else:
            table[arr[i]].append(i+1)

    return list(table.values())

print(anagrams(arr))
