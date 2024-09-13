# def checking(num):
#     return True if num == sum(i ** len(str(num)) for i in map(int, str(num))) else False
#
# print(*[i for i in range(1, int(input())) if checking(i)], sep='\n')
names = [input() for i in range(int(input()))]
summ = [(names[i], j) for i in range(len(names)) for j in names[i + 1:]]
print(summ)