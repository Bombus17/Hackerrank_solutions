#Author: 	Bombus17
#Purpose:	PlusMinus solution (Hackerrank - problem solving) 
#
#Challenge:	Given an array of integers, 
#			calculate the fractions of its elements that are positive, negative, and are zeros. 
#			Print the decimal value of each fraction on a new line.
# 


import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    counters = [0, 0, 0]

    for i in arr:
        if (i > 0):
            counters[0] += 1
            continue

        if (i < 0):
            counters[1] += 1
            continue

        counters[2] += 1

    for i in counters:
        print("%.6f" % (i / len(arr)))
