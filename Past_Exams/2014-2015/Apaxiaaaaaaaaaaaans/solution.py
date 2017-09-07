import sys

fhand = sys.stdin
lines = fhand.readlines()

name = lines[0].strip()
length = len(name)

c_temp = name[0]
name_compact = name[0]

for i in xrange(length):
    if name[i] != c_temp:
        name_compact += name[i]
        c_temp = name[i]

print(name_compact)


