# Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
# A = 710 ::: return AAH

def convertToTitle(num):
    my_dict = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    res = ""
    while num > 0:
        indx = num % 26
        res = my_dict[indx] + res
        num = num//26
        if indx == 0:
            num -= 1
    return res

print(convertToTitle(728))