import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

'''
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
'''

pwd = os.getcwd()

save_directory = os.path.join(pwd, 'paper/images/')
print(save_directory)


def f(x):
    return x**3-2*x**2

def e(x):
    return np.exp(-x**2)

x_values = np.arange(-5,5)

plt.figure()


plt.subplot(311)
plt.axis([-3, 3, -10, 10])
plt.plot(x_values, f(x_values))

plt.subplot(312)
plt.axis([-3, 3, -10, 10])
plt.plot(x_values, e(x_values))


plt.subplot(313)
plt.axis([-3, 3, -10, 10])
plt.plot(x_values, e(x_values)+f(x_values))

plt.show()


plt.savefig(save_directory + 'test.pdf', bbox_inches='tight')



