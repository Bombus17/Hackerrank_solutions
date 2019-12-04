#Author: 	Bombus17
#Purpose:	Diagnonal Difference solution (Hackerrank - problem solving) 
#
#Challenge:	Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#


import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    fst = 0
    sec = 0
    length = len(arr[0])
    for count in range(length):
        fst += arr[count][count]
        sec += arr[count][(length-count-1)]
    return abs(fst-sec)
