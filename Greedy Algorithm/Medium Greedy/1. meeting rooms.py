# Given an 2D array having size N X 2 denoting time intervals of different meeting
# arr[i][0] -> start time of ith meeting
# arr[i][1] -> end time of ith meeting

# Find minimum no of conference rooms require so that all meetings can be done
# Example: arr = [[1,18], [18,23], [15,29], [4,15], [2,11], [5,13]]
# Number of rooms required = 4
# room 1 -- [1,18], [18,23]
# room 2 -- [2,11], [15,29]
# room 3 -- [4,15]
# room 4 -- [5,13]

# Note: This question is similar to Hotel rooms possible from arrays

arr = [[1,18], [18,23], [15,29], [4,15], [2,11], [5,13]]
def solve(arr):
    rooms = 0
    time = [(t[0], 1) for t in arr] + [(t[1], 0) for t in arr]
    time.sort()
    count = 0
    for t in time:
        if t[1] == 1:
            count += 1
            rooms = max(rooms, count)
        else:
            count -= 1
    return rooms

print(solve(arr))


# Method 2: find maximum no of meetings that are going at a particular time
#               ------------
#           ----------------------     -------------
#       --------------           -------------------------------
#    -----------------------------------
# 0  1  2   4   5    11    13    15    18          23          29
#  
# clearly, at time = 5 there are max 4 meetings are going on.
# so we need at least 4 rooms to conduct these meetings

# Note: at time = 11, it is 3 meetings because meeting [2,11] just ends at time = 11

from collections import defaultdict
def solve(arr):
    noOfMeetings = defaultdict(lambda: 0)
    for start, end in arr:
        noOfMeetings[start] += 1
        noOfMeetings[end] -= 1
        
    rooms = count = 0
    times = sorted(list(noOfMeetings.keys()))
    for t in times:
        count += noOfMeetings[t]
        rooms = max([rooms, count])
    
    return rooms

print(solve(arr))


# Method 3: using min heap to calculate rooms
# iterate from start of the given array
# push end time (arr[i][1]) in the min heap. If start time >= top of heap (min end time)
# then replace it with end time of current meeting.  
import heapq
def solve(arr):
    arr.sort()
    heap = []
    for i in range(len(arr)):
        if heap and arr[i][0] >= heap[0]:
            heapq.heapreplace(heap, arr[i][1])
        else:
            heapq.heappush(heap, arr[i][1])
    return len(heap)

print(solve(arr))
