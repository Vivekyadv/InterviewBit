# There is a row of seats given in form of string, 'x' -> occupied, '.' unoccupied'
# There are people sitting in row, some are together and some are scattered
# You've to make the whole group sit together in such a way that total no of jumps to
# move them should be minimum.
           
# string = . x x . . . . x x x x . . . x . . . x x x . .
# person at seat_no 1 move to seat_no 6 in 5 jumps
# 2 to 5 in 3 jumps
# 15 to 11 in 3 jumps
# 19 to 12, 20 to 13, 21 to 14 in 6 jumps each
# Total ans = 6 + 6 + 6 + 3 + 3 + 5 = 29


# Method Explained: try to move every person near to the middle person. number of jumps
# required for this -> abs(seat_no[i] - seat_no[mid])  where seat_no[i] is seat no of
# ith person and seat_no[mid] - seat no of middle person
# AND make sure to subtract no of persons between ith person and middle person
# abs(i-mid)

def seats(string):
    mod = pow(10,7) + 3
    if "x" not in string or len(string) == 1:
        return 0
    
    seat_no = []
    for i in range(len(string)):
        if string[i] == 'x':
            seat_no.append(i)
    
    if seat_no == range(min(seat_no), max(seat_no)+1):
        return 0
    
    else:
        count = 0
        mid = len(seat_no)//2
        for i in range(len(seat_no)):
            diff = abs(seat_no[i]-seat_no[mid])
            indxDiff = abs(i-mid)
            count += diff - indxDiff
        return count % mod 

string = '.xx....xxxx...x...xxx..'
print(seats(string))
