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

while (j<Y-1):

	if (i>0) and (i<(X-1)):
		distance_0 = abs(elevation_map[i][j+1] - elevation_map[i][j])
		distance_1 = abs(elevation_map[i+1][j+1] - elevation_map[i][j])
		distance_2 = abs(elevation_map[i-1][j+1] - elevation_map[i][j])
		elevation_change_smallest = distance_0
		if distance_1 < elevation_change_smallest:
			elevation_change_smallest = distance_1
		if distance_2 < elevation_change_smallest:
			elevation_change_smallest = distance_2
		if distance_0 == elevation_change_smallest:
			i_next = i
			j_next = j+1
		elif distance_1 == elevation_change_smallest:
			i_next = i+1
			j_next = j+1
		else:
			i_next = i-1
			j_next = j+1

	elif i == 0:
		distance_0 = abs(elevation_map[i][j+1] - elevation_map[i][j])
		distance_1 = abs(elevation_map[i+1][j+1] - elevation_map[i][j])
		elevation_change_smallest = distance_0
		if distance_1 < elevation_change_smallest:
			elevation_change_smallest = distance_1
		if distance_0 == elevation_change_smallest:
			i_next = i
			j_next = j+1
		else:
			i_next = i+1
			j_next = j+1
	else:
		distance_0 = abs(elevation_map[i][j+1] - elevation_map[i][j])
		distance_2 = abs(elevation_map[i-1][j+1] - elevation_map[i][j])
		elevation_change_smallest = distance_0
		if distance_2 < elevation_change_smallest:
			elevation_change_smallest = distance_2
		if distance_0 == elevation_change_smallest:
			i_next = i
			j_next = j+1
		else:
			i_next = i-1
			j_next = j+1

	i = i_next
	j = j_next
	elevation_change_sum += elevation_change_smallest

print("%d %d %d" %(i, j, elevation_change_sum))
