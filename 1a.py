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
for i in a: 
    if i == '':
        mx = max(mx, cur)
        cur = 0 
    else:
        cur += int(i)
print(mx)