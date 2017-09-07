import sys

fhand = sys.stdin
lines = fhand.readlines()

n = int(lines[0].strip())

def mccarthy_91(n):
    if n > 100:
        return n-10
    else:
        return mccarthy_91(mccarthy_91(n+11))

print(mccarthy_91(n))