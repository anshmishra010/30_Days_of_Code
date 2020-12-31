#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    a = meal_cost*tip_percent
    b=a/100
    # print(b)
    c=tax_percent*meal_cost
    d=c/100
    # print(d)
    result = b+d+meal_cost
    # print(result)
    x = round(result)
    print(x)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)