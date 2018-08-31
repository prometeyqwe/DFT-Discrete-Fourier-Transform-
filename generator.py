import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


N = 600 # count of point
T = 1.0/300.0 # sampling frequency

x = np.linspace(0.0, N*T,N) # N*T - signal duration
a = np.sin(50.0 * 2.0*np.pi*x) # harmonic with frequency 50
b = 0.5*np.sin(80.0 * 2.0*np.pi*x) # harmonic with frequency 80 
c = 0.75*np.sin(100.0 * 2.0*np.pi*x) # harmonic with frequency 100

y=a+b+c #finished harmonic

plt.plot(x,y)
plt.grid()
# plt.show()

#------ writing data to file ------
f = open("input.txt", "w")
f.write(str(T))
for i in y:
    f.write("\t" + str(i))
#-----/ writing data to file ------
