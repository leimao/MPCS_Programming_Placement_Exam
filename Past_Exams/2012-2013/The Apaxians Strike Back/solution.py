import sys

fhand = sys.stdin
lines = fhand.readlines()

name = lines[0].strip()
first_character = name[0]

num_repetition = 0
for character in name:
    if character == first_character:
        num_repetition += 1
print num_repetition
