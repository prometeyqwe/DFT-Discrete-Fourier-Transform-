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
            output_arr[k] += float(input_arr[n])*exp(complex(0,(-2*pi*n*k)/N))
        k+=1

    return output_arr
#--------- /DFT -------------

# ------ reading from file------
input_file = open('input.txt', 'r')
input_str = input_file.read()
input_file.close()
input_arr = input_str.split("\t")
# ------ /reading from file------

# ------ using DFT ------
T = float(input_arr[0])#read T
N = len(input_arr)-1
input_arr=input_arr[1:N]
output = DFT(input_arr)
N = len(input_arr)
output_abs = [abs(i) for i in output]


plotx = np.linspace(0.0, 1/T,N)

plt.plot(plotx, output)
plt.grid()
plt.show()

plt.plot(plotx, output_abs)
plt.grid()
plt.show()
# ------ using DFT ------