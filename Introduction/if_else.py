'''
Task: Given an integer,n, perform the following conditional actions:
If n is odd, print Weird.
If n is even and in the inclusive range of 2 to 5, print Not Weird.
If n is even and in the inclusive range of 6 to 20, print Weird.
If n is even and greater than 20, print Not Weird.
'''
import math
import os
import random
import re
import sys

#import input
if __name__ == '__main__':
    n = int(raw_input().strip())

#Code
if n % 2 == 1:
    print ('Weird')
elif 2 <= n and n <= 5:
    print('Not Weird')
elif 6 <= n and n <= 20:
    print ('Weird')
elif n > 20:
    print('Not Weird')
    
