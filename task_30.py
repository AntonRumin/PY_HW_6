# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести
# с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print(' - - - Ввывод элементов арифметической прогресии - - -  ')

# Объявление переменных и ввод значений
first_n = int (input ('Введите первый элемент прогрессии: '))
dif = int (input ('Введите разность прогресии: '))
num_p = int (input ('Введите число элементов прогрессии: '))
ar_progress = list()

# Расчет элементов прогрессии и вывод каждого значения
print("Заданная Вами прогрессия содержит: ")
print()
for i in range (0, num_p):
    ar_progress.append(first_n + i * dif)
    print (f' Элемент {i + 1} - значение {ar_progress[i]}')
print ()

# Вывод всех элементов прогресии (списком)
print ('Элементы прогрессии (списком):')
print (ar_progress)

# Вывод всех  элементов прогресии
print ('Последовательность элементов прогрессии: ')
for element in ar_progress:
    print (f'{element}, ', end =" ")