'''
The University of Chicago
Master Program of Computer Science (MPCS)

Programming Placement Exam Problem
Python2 Solution for
"A Different Problem"

Problem Description:
https://uchicago.kattis.com/problems/different

Author: Lei Mao
Date: 7/13/2017
Last Revised: 7/13/2017
'''

import sys

# Use sys.stdin for input for most of the exam problems.
# To run the script in terminal, type "python solution.py < samples/sample.in".
# Note that '<' denotes the input file path.

for line in sys.stdin:
    [num_1, num_2] = line.split(' ')
    num_1 = int(num_1)
    num_2 = int(num_2)
    print abs(num_1 - num_2)
