Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np #імпорт бібліотеки
while True:
    while True:
        try:
            n, m = 4, 4         #створення матриці 4 на 4
            a = np.zeros((n, m), dtype=int)
            b = np.zeros((n, m), dtype=int)
            break
        except ValueError:
            print('Only nums')
    for i in range(n):          #задання значення для першої матриці
        for j in range(m):
            a[i, j] = int(input(f'A[{i},{j}]='))
            b[i,j] = a[i,j]
            if b[i,j] < 0:
                b[i,j] = 0      #перевод від'ємних значень в нолі
    print(f'Your matrix:\n{a}') #вивод матриці з від'ємним значенням
    print(f'Your new matrix without negative digits\n {b}')  #вивод матриці з нолями
    result = input('Хочете продовжити?Так-1,ні-інше')
    if result == '1':
        continue
    else:
        break
