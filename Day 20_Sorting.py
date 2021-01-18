#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


nos = 0

for i in range(n):

    for j in range(n - 1):
        if (a[j] > a[j + 1]):
            # temp = a[j]
            # a[j]=a[j+1]
            # a[j+1]= temp

            # we can both method to use swapping in Python

            a[j], a[j + 1] = a[j + 1], a[j]
            nos += 1

    if (nos == 0):
        break
print("Array is sorted in {} swaps.".format(nos))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
