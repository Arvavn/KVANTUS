import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()# создать поле для графиков

for i in range (10):
    file = open ('{}0 mm.txt'.format(i),'r')# r - read, w - write in file
    try:
    #file.readline(3)# считать N символов из текущую строки строки
        b = file.readlines()# запихать один файл в список из строк
        y = np.array(b[4:],int)# [] - обрезание
    finally:
        file.close() # закрыть файл
    x = np.arange(-50,50) # т.к максимально на 50-ом эле-е
    ax.plot(x,y)
    print(y)
plt.show()
#'string{0,1}'.format(i) # подставить в строку значение
