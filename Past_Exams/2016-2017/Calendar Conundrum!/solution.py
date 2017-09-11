import sys

fhand = sys.stdin
lines = fhand.readlines()

[a, b, c] = lines[0].strip().split(' ')
a = int(a)
b = int(b)
c = int(c)

def format_determine(a, b, c):
	if a > 31:
		return "Format #3"
	if (a > 12) and (a <= 31):
		if c > 31:
			return "Format #2"
		if c <= 31:
			return "Ambiguous"
	if a <= 12:
		if b > 12:
			return "Format #1"
		if b <= 12:
			return "Ambiguous"

print format_determine(a, b, c)