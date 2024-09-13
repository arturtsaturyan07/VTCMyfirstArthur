import sys
res = []
for line in sys.stdin:
    editing = [int(i) for i in line.split()]
    fill = lambda x: x % editing[0] != 0 and x % 100 // 10 == editing[-1] % 100 // 10
    print(*filter(fill, editing[1:-1]), sep='...')