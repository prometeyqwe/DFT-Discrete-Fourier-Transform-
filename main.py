from cmath import exp, pi
import matplotlib.pyplot as plt
import numpy as np
#--------- DFT -------------
def DFT(input_arr):
    N = len(input_arr)
    output_arr = [0 for i in range(N)]
    k=0
    n=0
    while k<N :
        for n in range(N):
            output_arr[k] += float(input_arr[n])*exp(complex(0,(-2*pi*n*k)/N)) #formula of DFT
        k+=
    return output_arr
#--------- /DFT -------------

# ------ reading from file------
input_file = open('input_file.txt', 'r')
input_str = input_file.read()
input_file.close()
input_arr = input_str.split("\t")
# ------ /reading from file------

# ------ using DFT ------
T = float(input_arr[0])#read T from file
N = len(input_arr)-1
input_arr=input_arr[1:N] 
output = DFT(input_arr)
N = len(input_arr)
output_abs = [abs(i) for i in output]

plotxsgn = np.linspace(0.0, N*T,N) # x for signal
plotxspec = np.linspace(-1/(2*T), 1/(2*T),N) # x for spectrum

for i in range(0,N/2): # normalization of spectrum, that null was is midlle
    temp = output_abs[i]
    output_abs[i] = output_abs[i+N/2]
    output_abs[i+N/2] = temp

plt.plot(plotxsgn, input_arr) # graph of signal
plt.xlabel("Time")
plt.ylabel("Amiplitude")
plt.title("Signal")
plt.grid()
plt.show()

plt.plot(plotxspec, output_abs) # graph of spectrum
plt.xlabel("Frequency")
plt.ylabel("Amiplitude")
plt.title("Spectrum")
plt.grid()
plt.show()
# ------ using DFT ------