
def correct_var(*args, change=1):
    global universe
    for line in args:
        func = lambda x: line.count(x) % 2 == change % 2
        print(*list(set(list(filter(func, line)))))
universe = (12.3, 8.0, 6.1, 0.2)
data = ["GREAT TURTLE", "multiverse",
"FLOAT TO LAF"]
result = correct_var(*data)
iter(None)