#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

maxvalue = -2 ** 31
# this is the lowest possible integer value can be stored , as sometimes value can contain negative int as a sum thats why we did'nt use maxvalue as 0
for i in range(4):
    for j in range(4):
        a = arr[i][j]
        b = arr[i][j + 1]
        c = arr[i][j + 2]
        d = arr[i + 1][j + 1]
        e = arr[i + 2][j]
        f = arr[i + 2][j + 1]
        g = arr[i + 2][j + 2]

        value = a + b + c + e + d + f + g
        if (maxvalue < value):
            maxvalue = value
print(maxvalue)