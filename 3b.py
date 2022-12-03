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
for i in range(0, len(a) - 1, 3):
    x, y, z = set(a[i]), set(a[i+1]), set(a[i+2])
    for l in x: 
        if l in y and l in z:
            if l.islower():
                b += ord(l) - ord('a') + 1 
            else:
                b += ord(l) - ord('A') + 27
print(b)