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
    sc += z[n]
    if (n == 'X' and m == 'C') or (n == 'Y' and m == 'A') or (n == 'Z' and m == 'B'):
        sc += 6
    elif (n == 'X' and m == 'A') or (n == 'Y' and m == 'B') or (n == 'Z' and m == 'C'):
        sc += 3 
print(sc)