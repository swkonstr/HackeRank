#!/bin/python3

import sys

n = int(input().strip())

str = bin(n)
print (str)
m=1
mm=1
for i in range(len(str)-1):
    print (i)
    if (str[i]=="1") and (str[i+1]=="1"):
        mm+=1
        print ("m=", m, "mm=", mm)
    else:
        mm=1
    if (mm>m):
        m=mm
        print ("m=", m, "mm=", mm)

print (m)