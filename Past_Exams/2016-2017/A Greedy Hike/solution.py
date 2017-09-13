import sys

fhand = sys.stdin
lines = fhand.readlines()

[X, Y] = lines[0].strip().split(' ')
X = int(X)
Y = int(Y)
[xs, ys] = lines[1].strip().split(' ')
xs = int(xs)
ys = int(ys)

elevation_map = list()
for i in xrange(X):
	elevations = lines[i+2].strip().split(' ')
	for j in xrange(Y):
		elevations[j] = int(elevations[j])
	elevation_map.append(elevations)

i = xs
j = ys
elevation_change_sum = 0

while (j<(Y-1)):

	# Initialize distance
	distance_0 = float('inf')
	distance_1 = float('inf')
	distance_2 = float('inf')
	# Get elevation change if exists
	distance_0 = abs(elevation_map[i][j+1] - elevation_map[i][j])
	if (i+1) < X:
		distance_1 = abs(elevation_map[i+1][j+1] - elevation_map[i][j])
	if (i-1) >= 0:
		distance_2 = abs(elevation_map[i-1][j+1] - elevation_map[i][j])
	elevation_change_smallest = distance_0
	i_next = i
	if distance_1 < elevation_change_smallest:
		elevation_change_smallest = distance_1
		i_next = i+1
	if distance_2 < elevation_change_smallest:
		elevation_change_smallest = distance_2
		i_next = i-1

	j_next = j+1
	elevation_change_sum += elevation_change_smallest

	i = i_next
	j = j_next


print("%d %d %d" %(i, j, elevation_change_sum))
