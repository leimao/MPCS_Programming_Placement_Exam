'''
The University of Chicago
Master Program of Computer Science (MPCS)
2015-2016
Programming Placement Exam Problem
Python2 Solution for
"What's in an (Apaxian) Name"

Problem Description: https://uchicago.kattis.com/problems/uchicagoplacement.apaxiannames

Author: Lei Mao
Date: 7/13/2017
Last Revised: 7/13/2017
'''

import sys

fhand = sys.stdin

lines = fhand.readlines()

community = lines[0].strip()

# The number of Apaxian names
N = int(lines[1].strip())

# 0: princess; 1: baron; 2: priest; 3: commoner
def classification(name, community):
    if name[0:len(community)] == community:
        return 0
    elif name[-len(community):] == community:
        return 1
    for i in xrange(1,len(name)-len(community)):
        if name[i:i+len(community)] == community:
            return 2
    return 3

class_count = [0] * 4
for i in xrange(2, 2+N):
    name = lines[i].strip()
    class_count[classification(name = name, community = community)] += 1
    
print("%d PRINCESS" %class_count[0])
print("%d BARON" %class_count[1])
print("%d PRIEST" %class_count[2])
print("%d COMMONER" %class_count[3])
