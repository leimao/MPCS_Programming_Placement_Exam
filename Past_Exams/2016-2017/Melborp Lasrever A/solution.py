import sys

fhand = sys.stdin
lines = fhand.readlines()

string = lines[0].strip()

def string_reverse(string):
	if len(string) == 1:
		return string[0]
	else:
		return string_reverse(string[1:]) + string[0]

print string_reverse(string)