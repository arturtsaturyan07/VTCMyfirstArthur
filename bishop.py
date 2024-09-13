class X:
    def __call__(self, a):
        return a


class SQRT_X:
    def __call__(self, a):
        return a ** 0.5


class Expression:
    def __init__(self, f1, f2, op):
        self.f1 = f1
        self.f2 = f2
        self.op = op

    def __call__(self, a):
        if self.op == '+':
            return self.f1(a) + self.f2(a)
        elif self.op == '-':
            return self.f1(a) - self.f2(a)
        elif self.op == '/':
            return self.f1(a) / self.f2(a)
        elif self.op == '*':
            return self.f1(a) * self.f2(a)

n = int(input())
functions = {'x': X(), 'sqrt_fun': SQRT_X()}
for _ in range(n):
    line = input().split()
    if line[0] == 'calculate':
        values = [functions[line[1]](int(b)) for b in line[2:]]
        print(*values)
    elif line[0] == 'define':
        f = Expression(functions[line[2]], functions[line[4]], line[3])
        functions[line[1]] = f
