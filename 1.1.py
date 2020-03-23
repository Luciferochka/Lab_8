Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотньому порядку
import numpy as np
while True:
    while True:
        try:
            n = int(input('Enter amount of digits'))  
            a = np.zeros((n), dtype=int)    #місце для масива
            b = np.zeros((n), dtype=int)    #місце для масива
            break
        except ValueError:   #перевірка на помилки(тільки цифри)
            print('Тільки цифри')

    for i in range(n):
        a[i] = int(input('Enter your digits: '))    #ввод цифр
    print(a)

    for i in range(n):
        b[i] = a[n - 1 - i]#вивод значення в зворотному порядку
    print(f'New array:{b}')
    result = input('Хочете продовжити?Так-1,ні-інше')
    if result == '1':
        continue
    else:
        break#виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотньому порядку
import numpy as np #імпорт бібліоетки
while True:
    while True:
        try:
            n = int(input('Enter amount of digits'))  #
            a = np.zeros((n), dtype=int)    #місце для масива
            b = np.zeros((n), dtype=int)    #місце для масива
            break
        except ValueError:   #перевірка на помилки(тільки цифри)
            print('Тільки цифри')

    for i in range(n):
        a[i] = int(input('Enter your digits: '))    #ввод цифр
    print(a)

    for i in range(n):
        b[i] = a[n - 1 - i]#вивод значення в зворотному порядку
    print(f'New array:{b}')
    result = input('Хочете продовжити?Так-1,ні-інше')
    if result == '1':
        continue
    else:
        break
