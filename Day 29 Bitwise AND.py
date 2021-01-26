#!/bin/python3

import math
import os
import random
import re
import sys

def bt(n,k):
    t_b=0
    for b in range(1,n+1):
        for a in range(1,b):
            bit = a & b
            if t_b<bit<k:
                t_b=bit
                if t_b == k-1:
                    return t_b
    return t_b


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        print(bt(n,k))
