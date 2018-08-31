from cmath import exp, pi
import matplotlib.pyplot as plt
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
input_file = open('input_data.txt', 'r')
input_str = input_file.read()
input_file.close()
input_arr = input_str.split("\t")
# print(input_arr)
# ------ /reading from file------


# ------ using DFT ------
dl = 5
output = DFT(input_arr)
N = len(output)
output_abs = [abs(i) for i in output]

# print output_abs

plotx = [i/dl - N/dl/2 for i in range(N)]

plt.plot(plotx, input_arr)
plt.grid()
plt.show()

plt.plot(plotx, output_abs)
plt.grid()
plt.show()

# ------ using DFT ------