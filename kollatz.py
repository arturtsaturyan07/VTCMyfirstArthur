def defractalize(fractal):
    f = fractal.copy()
    fractal.clear()
    for i in f:
        if type(i) != type(fractal):
            fractal.append(i)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)