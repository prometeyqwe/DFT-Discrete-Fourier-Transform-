import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import random

count = input("Enter count of waves: ")
freq_arr = [0 for i in range(count)]
weight_arr = [0 for i in range(count)]

for i in range(count): # create random frequency for harmonics
    freq_arr[i] = random.randint(1,count*10)
print "gen freq: "
print freq_arr

for i in range(count): # create random weight for harmonics
    weight_arr[i] = random.randint(0,count*2)
print "gen weight: "
print weight_arr

N = 600 # count of points
T = 1.0/float(3*max(freq_arr)) # calculation of the sampling rate
harmonic_arr = [0.0 for i in range(N)] # arr for once harmonic
final_harmonic = [0.0 for i in range(N)] # arr for final harmonic = sum of random harmonic
x = np.linspace(0.0, N*T,N) # N*T - signal duration

for i in range(count): # receiving final harmonic
    harmonic_arr = weight_arr[i]*np.sin(float(freq_arr[i]) * 2.0*np.pi*x)
    final_harmonic += harmonic_arr

#----- if you want create your dataset || example -----
# a = np.sin(55.0 * 2.0*np.pi*x) # harmonic with frequency 50
# b = 0.5*np.sin(25.0 * 2.0*np.pi*x) # harmonic with frequency 80 
# c = 0.75*np.sin(50.0 * 2.0*np.pi*x) # harmonic with frequency 100
# y=a+b+c #finished harmonic
#----/ if you want create your dataset || example -----

#---- graph final garmonic ----
plt.plot(x,final_harmonic)
plt.grid()
plt.xlabel("Time")
plt.ylabel("Amiplitude")
plt.title("Signal")
plt.show()
#---/ graph final garmonic ----

#------ writing data to file ------
f = open("input.txt", "w")
f.write(str(T))
for i in final_harmonic:
    f.write("\t" + str(i))
#-----/ writing data to file ------
