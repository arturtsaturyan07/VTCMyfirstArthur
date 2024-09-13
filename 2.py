import sys
a = 1
res = []
for lines in sys.stdin:
    line = list(map(int, lines.strip().split(', ')))
    res.append(([i for i in line if i % 2 == 0], len([i for i in line if i % 2 == 0]), a))
    a += 1
mylist = sorted(res, key=lambda x: (x[1], -x[2]))
print(mylist[-1][0])