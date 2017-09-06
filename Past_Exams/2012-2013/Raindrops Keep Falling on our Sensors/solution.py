import sys

fhand = sys.stdin
lines = fhand.readlines()

num_measurements = int(lines[0].strip())
measurements = lines[1].strip().split(' ')

for i in xrange(num_measurements):
    measurements[i] = int(measurements[i])

sum_valid_measurements = 0
num_valid_measurements = 0
for measurement in measurements:
    if measurement >= 0:
        sum_valid_measurements += measurement
        num_valid_measurements += 1

if num_valid_measurements == 0:
    print "INSUFFICIENT DATA"
else:
    print int(sum_valid_measurements/num_valid_measurements)

