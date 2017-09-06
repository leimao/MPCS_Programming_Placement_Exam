import sys

fhand = sys.stdin
lines = fhand.readlines()

x = int(lines[0].strip().split(' ')[0])
n = int(lines[0].strip().split(' ')[1])

def exp(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif (n > 1) and (n % 2 == 0):
        return exp(x*x, n/2)
    elif (n > 1) and (n % 2 != 0):
        return exp(x*x, (n-1)/2) * x

print(exp(x = x, n = n))