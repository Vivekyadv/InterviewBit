# Given two arrays position of mice and position of holes. Each hole can accomodate only
# 1 mouse. mouse can stay at his position, move one step forward, or move one step
# backward. Any of these moves take 1 min of time. Assign mice to holes so that the time 
# when the last mouse gets inside a hole is minimized.


# Method: sort both arrays and find max of abs(a[i]- b[i])
# Why sorting? write down position of mice and position of holes on a straight line 
# and you'll understand why sorting is necessary 
def mice(micPos, holePos):
    micePos.sort()
    holePos.sort()
    maxTime = 0
    for i in range(len(micePos)):
        maxTime = max(maxTime, abs(micPos[i]-holePos[i]))
    return maxTime

micePos = [-10, -79, -79, 67, 93, -85, -28, -94]
holePos = [-2, 9, 69, 25, -31, 23, 50, 78]
print(mice(micePos, holePos))

