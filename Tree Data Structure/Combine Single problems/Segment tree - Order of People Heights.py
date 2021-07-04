# Given heights and infronts array of integers
# Heights : A list of heights of N persons standing in a queue
# Infronts : A list of numbers corresponding to each person (P) that gives the 
# number of persons who are taller than P and standing in front of P

# You need to return list of actual order of persons’s height
# Example:   Heights = [5, 3, 2, 6, 1, 4] and InFronts = [0, 1, 2, 0, 3, 2]
# Output, actual order of heights is =  [5, 3, 2, 1, 6, 4]


def order(heights, inFronts):
    n = len(heights)
    table = {heights[i] : inFronts[i] for i in range(n)}

    positions = list(range(n))
    res = [-1]*n

    for k in sorted(table.keys()):
        inFr = table[k]
        pos_inFr = positions[inFr]
        res[pos_inFr] = k
        del positions[inFr]

    return res

heights = [5, 3, 2, 6, 1, 4]
inFronts = [0, 1, 2, 0, 3, 2]
print(order(heights, inFronts))