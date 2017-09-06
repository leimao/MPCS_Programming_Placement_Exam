import sys

fhand = sys.stdin
lines = fhand.readlines()

num_measurements = int(lines[0].strip())

measurements = lines[1].strip().split()
for i in xrange(num_measurements):
    measurements[i] = int(measurements[i])

measurement_max = measurements[0]
measurement_min = measurements[0]

for measurement in measurements:
    if measurement > measurement_max:
        measurement_max = measurement
    if measurement < measurement_min:
        measurement_min = measurement

print(measurement_max -measurement_min)