import sys

fhand = sys.stdin
lines = fhand.readlines()

[first_name, last_name] = lines[0].strip().split(' ')

if len(last_name) == 5:
	last_name = last_name * 4
else:
	last_name = last_name * len(last_name)

print("%s %s" %(first_name, last_name))