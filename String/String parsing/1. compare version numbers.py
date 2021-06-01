# Given two version numbers. If version1 > version2 return 1,
# If version1 < version2 return -1, otherwise return 0.
# example of version num ordering: 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

# Logic: split versions on (.) and then compare them

def compareVersion(ver1, ver2):
    ver1 = list(map(int, ver1.split('.')))
    ver2 = list(map(int, ver2.split('.')))

    # put 0's at the starting of smaller number
    while len(ver1) < len(ver2):
        ver1.append(0)
    while len(ver2) < len(ver1):
        ver2.append(0)
    
    # compare these version numbers
    for i in range(len(ver1)):
        if ver1[i] < ver2[i]:
            return -1
        if ver1[i] > ver2[i]:
            return 1
    return 0

ver1 = "13.0"
ver2 = "13.0.8"
print(compareVersion(ver1, ver2))
