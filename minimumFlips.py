'''
Take in initial string of all zeroes (e.g. '000000'). Target string is the same length and can be combination of '1's and '0's (e.g. '101010).
When a value is flipped to the opposite digit, every value to the right is also flipped.
Find minimum number of flips to reach target string.
'''

def minFlips(target):
    digit = '1'
    flips = 0
    
    for i in range(len(target)):
        if target[i] == digit:
            flips += 1
            digit = str((int(digit) + 1) % 2)
    
    return flips

print(minFlips('0011'))
print(minFlips('10101'))