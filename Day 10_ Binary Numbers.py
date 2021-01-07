#!/bin/python3

import math
import os
import random
import re
import sys


# c=current
# m=maximum or total
if __name__ == '__main__':
    n = int(input())
    c=0
    m=0
    while(n>0):
        r=n%2
        if(r==1):
            c+=1
            if(c>m):
                m=c
        else:
            c=0
        n=n//2

    print(m)