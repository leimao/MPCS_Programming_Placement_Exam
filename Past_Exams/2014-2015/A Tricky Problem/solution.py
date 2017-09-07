import sys

fhand = sys.stdin
lines = fhand.readlines()

N = int(lines[0].strip())
card_A = lines[1].strip().split(' ')
card_B = lines[2].strip().split(' ')

card_value ={
'2':1,
'3':2,
'4':3,
'5':4,
'6':5,
'7':6,
'8':7,
'9':8,
'J':9,
'Q':10,
'K':11,
'A':12,
}

point_A = 0
point_B = 0

for i in xrange(N):
    if card_value[card_A[i]] > card_value[card_B[i]]:
        point_A += 1
    elif card_value[card_A[i]] < card_value[card_B[i]]:
        point_B += 1

if point_A > point_B:
    print("PLAYER 1 WINS")
elif point_A < point_B:
    print("PLAYER 2 WINS")
else:
    print("TIE")
