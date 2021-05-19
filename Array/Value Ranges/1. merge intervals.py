# Given a set of non-overlapping intervals, 
# insert a new interval into the intervals (merge if necessary).

# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] 
# would result in [1,2],[3,10],[12,16].

def mergeintervals(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])
    overlapped = []
    for intrvl in intervals:
        if overlapped and intrvl[0] <= overlapped[-1][1]:
            overlapped[-1][1] = max(overlapped[-1][1], intrvl[1])
        else:
            overlapped.append(intrvl)
    print(overlapped)

arr = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_arr = [4,9]
mergeintervals(arr,new_arr)    