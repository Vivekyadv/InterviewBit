# Given n light bulbs which are connect in series. The wire is faulty, a switch changes the
# state of all bulbs to the right of it. Given an initial state of all bulbs, 
# find the minimum number of switches you have to press to turn on all the bulbs. 

# arr = [0, 1, 1, 0, 1] Expected output is 4
# Explanation: 
# 1st press 1 0 0 1 0
# 2nd press 1 1 1 0 1
# skip the third switch, it is already on
# 3rd press 1 1 1 1 0
# 4th press 1 1 1 1 1       total no of presses = 4


# Logic: start the no of presses (nop) as 0
# if nop is even, state of element will remain as it was given. So, if arr[i] = 0, press it
# if nop is odd, state of element will be reversed. So if arr[i] = 1 (it was 0) press it

def bulbs(arr):
    nop = 0
    for i in range(len(arr)):
        if nop % 2 == 0:
            if arr[i] == 0:
                # press it
                nop += 1
        else:
            if arr[i] == 1:
                nop += 1
    return nop

# for loop in the above code can be written as
# for i in range(len(arr)):
#     if nop % 2 == arr[i]:
#         nop += 1

arr = [0, 1, 1, 0, 1]
print(bulbs(arr))
