import sys

fhand = sys.stdin
lines = fhand.readlines()

a = int(lines[0].strip().split(' ')[0])
b = int(lines[0].strip().split(' ')[1])

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

print gcd(a = a, b = b)