import sys

fhand = sys.stdin
lines = fhand.readlines()

x = int(lines[0].strip().split(' ')[0])
y = int(lines[0].strip().split(' ')[1])

mine_map = list()
for i in xrange(x):
    mine_map_line = lines[1+i].strip().split(' ')
    for j in xrange(y):
        mine_map_line[j] = int(mine_map_line[j])
    mine_map.append(mine_map_line)

mine_solution = list()
for i in xrange(x):
    mine_solution_line = list()
    for j in xrange(y):
        if mine_map[i][j] == 1:
            mine_solution_line.append('X')
        else:
            num_mines = 0
            if (i-1) >= 0:
                num_mines += mine_map[i-1][j]
                if (j-1) >= 0:
                    num_mines += mine_map[i-1][j-1]
                if (j+1) < y:
                    num_mines += mine_map[i-1][j+1]
            if (i+1) < x:
                num_mines += mine_map[i+1][j]
                if (j-1) >= 0:
                    num_mines += mine_map[i+1][j-1]
                if (j+1) < y:
                    num_mines += mine_map[i+1][j+1]
            if (j-1) >= 0:
                num_mines += mine_map[i][j-1]
            if (j+1) < y:
                num_mines += mine_map[i][j+1]
            if num_mines == 0:
                mine_solution_line.append('-')
            else:
                mine_solution_line.append(str(num_mines))
    mine_solution.append(mine_solution_line)

for i in xrange(x):
    print_line = ''
    for j in xrange(y):
        print_line += mine_solution[i][j]
    print print_line

