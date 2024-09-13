import matplotlib.pyplot as plt
import numpy as np
n = int(input("input "))
fig, ax = plt.subplots()

a = []
for i in range(n):
    a += [int(input("ներմուծել սկզբնական անկյունը  = "))]
v = []
for i in range(n):
    v += [int(input("ներմուծել սկզբնական արագությունը = "))]
g = 9.8
xmax = 2 * np.cos(np.radians(a)) * np.sin(np.radians(a)) * v * v / g
ymax = (v * np.sin(np.radians(a))) ** (2) / (2 * g)
x = np.linspace(0, xmax, 100)
y = x * np.tan(np.radians(a)) - (g * x ** (2)) / (2 * (np.cos(np.radians(a)) * v) ** (2))
print("S(max) = ", ''.join(list(str(xmax))), " H(max) =", ''.join(list(str(ymax))))
ax.set_title('Ֆունկցիայի գրաֆիկ')
ax.set_xlabel('s')
ax.set_ylabel('h')
ax.plot(x, y)
plt.grid(True)
plt.show()
