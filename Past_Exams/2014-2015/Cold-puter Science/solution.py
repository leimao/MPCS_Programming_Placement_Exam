import sys

fhand = sys.stdin
lines = fhand.readlines()

num_days = int(lines[0].strip())
num_days_below_zero = 0
temperatures = lines[1].strip().split()

for temperature in temperatures:
    if int(temperature) < 0:
        num_days_below_zero += 1

print num_days_below_zero

