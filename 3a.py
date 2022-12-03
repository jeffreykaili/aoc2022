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
for l in a:
    first = set(l[:len(l) // 2])
    rest = set(l[len(l) // 2:])
    for x in first:
        if x in rest:
            if x.islower():
                b += ord(x) - ord('a') + 1 
            else:
                b += ord(x) - ord('A') + 27
print(b)