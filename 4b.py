from math import* 
from itertools import*
from collections import*
import fileinput 
global a 
a = []
b = 0 
c = 0 
def rl(): 
    f = open("AOC.txt").readlines()
    global a 
    for line in f:
        a.append(line.strip())

rl() 
for line in a:
    f = line.split(",")[0]
    s = line.split(",")[1]
    x,y = map(int,f.split("-"))
    a,b = map(int,s.split("-"))
    if (x <= a and y >= a) or (a <= x and b >= x) or (x <= b and y >= b) or (a <= y and b >= y):
        c += 1
print(c)