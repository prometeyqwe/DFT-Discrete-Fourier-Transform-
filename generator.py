import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


N = 600
T = 1.0/200.0
x = np.linspace(0.0, N*T,N)
a = np.sin(50.0 * 2.0*np.pi*x)
b = 0.5*np.sin(80.0 * 2.0*np.pi*x)
c = 0.75*np.sin(100.0 * 2.0*np.pi*x)

y=a+b+c

plt.plot(x,y)
plt.grid()
# plt.show()

f = open("input.txt", "w")
f.write(str(T))
for i in y:
    f.write("\t" + str(i))

