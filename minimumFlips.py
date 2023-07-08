'''
Take in initial string of all zeroes (e.g. '000000'). Target string is the same length and can be combination of '1's and '0's (e.g. '101010).
When a value is flipped to the opposite digit, every value to the right is also flipped.
Find minimum number of flips to reach target string.
'''

def minFlips(target):
    digit = '1'
    flips = 0
    
    for num in target:
        if num == digit:
            flips += 1
            if digit == '1':
                digit == '0'
            else:
                digit == '1'
    
    return flips

print(minFlips('0011'))
print(minFlips('10101'))
# 0000
# 0011


# 11111
# 10000
# 10111
# 10100
# 10101

# 00001
# 00110
# 01001
# 10110
# 10101