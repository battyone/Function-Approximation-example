import numpy as np
from scipy import sin, exp
from scipy.linalg import solve
from matplotlib import pyplot as plt

p = np.arange(1, 16)


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


a = [[x**n for n in range(len(p))] for x in p]
b = [f(x) for x in p]

s1 = solve(a, b)
print(s1)
plt.plot(p, b, 'd', p, b, '----')
plt.show()