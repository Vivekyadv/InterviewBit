# The string "PAYPALISHIRING" is written in zigzag pattern on given
# number of rows like this: 
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R

def convert(string, rows):
    if rows ==1 or len(string) == 1:
        return string
    n = len(string)
    listAns = [list() for i in range(rows)]
    row = 0
    isFirst = True
    for i in range(n):
        listAns[row].append(string[i])
        if rows != 1:
            if row == 0:
                isFirst = True
            elif row == rows-1:
                isFirst = False
            if isFirst:
                row += 1
            else:
                row -= 1
    ans = []
    for elements in listAns:
        ans.append(''.join(elements))
    return ''.join(ans)


string = "PAYPALISHIRING"
rows = 3
print(convert(string, rows))