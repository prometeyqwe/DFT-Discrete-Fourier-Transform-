input_file = open('input_data.txt', 'r')
input_str = input_file.read()
input_file.close()
input_arr = input_str.split("\n")
print(input_arr)


