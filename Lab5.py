# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
# сравнительного вычисления данной функции рекурсивно и итерационно. Определить (смоделировать) 
# границы применимости рекурсивного и итерационного подхода. 
# Вариант 24
# F(0) = F(1) = 11, F(n) = 3*F(n–1) - F(n-2), при n > 1
#import math
import time # импорт библиотек
import matplotlib.pyplot as mpl

while True:
    n = int(input("Введите натуральное число n>=0: "))
    if n >=0:
        break
    else:
        print("Введено неверное число!")

def F_iter(n): #Итерационное решение
    F = [0 for i in range(n+1)]
    F[0] = 11
    F[1] = 11
    for i in range(n+1):
        F[i] = 3*F[i-1] - F[i-2]
    return F[n]

def F_rec(n): #Рекурсивное решение
    if n == 1 or n == 0:
        return 11
    elif n > 1:
        return 3*F_rec(n-1) - F_rec(n-2)

rec_times = []  # создание списков для построения таблицы значений
rec_values = []
iter_times = []
iter_values = []
n_values = list(range(1, n + 1))

for n in n_values: # заполнение списков
    t0 = time.time()
    iter_values.append(F_iter(n))
    t1 = time.time()
    iter_times.append(t1-t0)
    rec_values.append(F_rec(n))
    t2 = time.time()
    rec_times.append(t2-t1)

table = []  # Таблица значений
for i, n in enumerate(n_values):
    table.append([n, rec_times[i], iter_times[i], rec_values[i], iter_values[i]])
print('{:<4}|{:<25}|{:<25}|{:<25}|{:<25}'.format('n', 'Время рекурсии', 'Время итерации', 'Значение рекурсии', 'Значение итерации'))  # вывод таблицы
print('-' * 105)
for data in table:
    print('{:<4}|{:<25}|{:<25}|{:<25}|{:<25}'.format(data[0], data[1], data[2], data[3], data[4]))

mpl.plot(n_values, iter_times, label='Итерация')
mpl.plot(n_values, rec_times, label='Рекурсия')  # вывод графиков
mpl.xlabel('n')
mpl.ylabel('Время (с)')
mpl.title('Сравнение времени рекурсивного и итерационного подхода')
mpl.legend()
mpl.show()
