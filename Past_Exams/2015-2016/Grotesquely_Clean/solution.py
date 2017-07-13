'''
The University of Chicago
Master Program of Computer Science (MPCS)
2015-2016
Programming Placement Exam Problem
Python2 Solution for
"Grotesquely Clean"

Problem Description: https://uchicago.kattis.com/problems/uchicagoplacement.grotesque

Author: Lei Mao
Date: 7/13/2017
Last Revised: 7/13/2017
'''

import sys

require_clean = False

fhand = sys.stdin
lines = fhand.readlines()

dirtiness = list()
for measurement in lines[0].split():
    dirtiness.append(int(measurement))
    if int(measurement) == 6:
        require_clean = True

if require_clean == False:
    if sum(dirtiness) >= 30:
        require_clean = True
    else:
        require_clean = False

if require_clean == True:
    print("CLEAN")
else:
    print("DO NOT CLEAN")