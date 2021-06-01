# Given roman number, convert it into decimal form

def romanToInt(roman):
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    n = len(roman)
    for i in range(n-1):
        if convert[roman[i]] < convert[roman[i+1]]:
            decimal -= convert[roman[i]]
        else:
            decimal += convert[roman[i]]
    decimal += convert[roman[n-1]]
    return decimal

print(romanToInt("XLIX"))