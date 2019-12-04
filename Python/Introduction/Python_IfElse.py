#Author: 	Bombus17
#Purpose:	PlusMinus solution (Hackerrank - Python challenges) 
#
#Challenge:	Given an integer, , perform the following conditional actions:
#			If  is odd, print Weird
#			If  is even and in the inclusive range of  to , print Not Weird
#			If  is even and in the inclusive range of  to , print Weird
#			If  is even and greater than , print Not Weird
# 


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n % 2 == 0:
        if n in range(2,5+1):
            print("Not Weird")
        elif n in range(2,20+1):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
