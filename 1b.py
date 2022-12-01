global a
a = [] 
def rl(): 
    f = open("AOC.txt").readlines()
    global a 
    for line in f:
        a.append(line.strip())
rl()
mx = 0 
cur = 0 
b = []
for i in a: 
    if i == '':
        b.append(cur)
        cur = 0 
    else:
        cur += int(i)
b.sort()
print(b[-1] + b[-2] + b[-3])