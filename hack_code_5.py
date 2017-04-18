#!/bin/python3

import sys


n = int(input().strip())

idx=1
sum=0
while idx < 11:
    print (n, "x", idx, "=", n * idx)
    idx += 1