#Author: 	Bombus17
#Purpose: 	Solution for A Very Big Sum (Hackerrank - Problem Solving)
#
#Challenge: Calculate and print the sum of the elements in an array, 
#			keeping in mind that some of those integers may be quite large.
#


import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    result = 0
    for i in range(len(ar)):
        result+=ar[i]
    return result



