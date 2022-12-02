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
z = {'A' : 1, 'B' : 2, 'C' : 3}
sc = 0 
for x in a:
    m, n = x.split()
    if n == 'X':
        if m == 'A':
            sc += 3 
        elif m == 'B':
            sc += 1 
        else:
            sc += 2 
    elif n == 'Y':
        sc += 3 + z[m]
    else:
        sc += 6 
        if m == 'A':
            sc += 2 
        elif m == 'B':
            sc += 3 
        else:
            sc += 1 
print(sc)