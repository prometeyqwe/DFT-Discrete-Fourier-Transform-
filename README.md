# DFT-Discrete-Fourier-Transform-
## Algorithm of Discrete Fourier Transform
## Russian
## Описание
#####
Это программа производит Дискретное Фурье Преобразование, на вход программе поступает какой-либо сигнал, на выходе же получается спектральная плотность этого сигнала. Для наглядности ее работы строятся графики. 
######
Для демонстрации работы программы можно использовать готовые наборы данных (input_file_1.txt, input_file_2.txt), для этого измените название файла в main.py в строке 18. 
######
Также в программу добавлен генератор суммы синусоидальных сигналов, для работы с ним, замените название файла в 18 строке на input.txt, и воспользуйтесь генератором(generator.py), на входе в программу требуется ввести необходимое вам количество грамоник, далее программа псевдослучайным образом подберет для каждой гармоники значения веса и несущей частоты, также построит полученный сигнал. Теперь можно использовать main.py, для определения спектральной плотности только что полученного сигнала.
######
При необходимости вы можете самостоятельно составить необходимые вам гармоники, для этого раскомментируйте строки 30-35 и в строке 38, 49 замените final_harmonic -> y. 
######
Также приведены изображение демонстрирующие объявленные выше наборы данных(input_1.png, input_2.png, output_1.png, output_2.png).
######
## Информация по наборам данных
### Набор данных 1:
    Количество гармоник: 3
    Частоты: 25, 50, 55
    Веса: 0.5, 0.75, 1
### Набор данных 2:
    Количество гармоник: 5
    Частоты: 9, 40, 24, 2, 38
    Веса: 5, 4, 9, 4, 1

Вы можете самостоятельно составить такие гармоники и получить такой же результат для спектральной плотности как в приведенных изображениях. Как это сделать говорилось выше.
######
## English, GoogleTranslater
## Description
This program produces a Discrete Fourier Transformation, the input to the program receives a signal, the output is the spectral density of this signal. For clarity of its work schedules are constructed.
######
To demonstrate the operation of the program, you can use ready-made data sets (input_file_1.txt, input_file_2.txt), for this change the file name in main.py on line 18.
######
Also the generator of the sum of sinusoidal signals is added to the program, to work with it, replace the file name in the 18 line with the input.txt, and use the generator (generator.py), at the entrance to the program it is required to enter the necessary number of grammars, then the program pseudo-randomly selects for each harmonic of the weight value and the carrier frequency, will also build the received signal. Now you can use main.py to determine the spectral density of the signal just received.
######
If necessary, you can independently compose the harmonics you need, for this uncomment lines 30-35 and on line 38, 49 replace final_harmonic -> y.
######
Also an image is shown showing the previously announced data sets (input_1.png, input_2.png, output_1.png, output_2.png).
######
## Information on data sets
### Data set 1:
     Number of harmonics: 3
     Frequencies: 25, 50, 55
     Weights: 0.5, 0.75, 1
### Data set 2:
     Number of harmonics: 5
     Frequencies: 9, 40, 24, 2, 38
     Weights: 5, 4, 9, 4, 1

You can independently compose such harmonics and obtain the same result for spectral density as in pr