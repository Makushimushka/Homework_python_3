import math


# ## 1.	Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# -	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def task_01(our_list = [2, 3, 5, 9, 3]):
    result = 0
    odd_numbers = []
    for i in range(1, len(our_list), 2):
        result += our_list[i]
        odd_numbers.append(our_list[i])
    print("на нечётных позициях элементы  {}. Ответ: ".format(", ".join(str(x) for x in odd_numbers)), result)
task_01()


def task_01_1(our_list = [2, 3, 5, 9, 3]):
    odd_numbers = our_list[1::2]
    print("на нечётных позициях элементы  {}. Ответ: ".format(", ".join(str(x) for x in odd_numbers)), sum(odd_numbers))

task_01_1()


# ## 2.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     
#  - [2, 3, 4, 5, 6] => [12, 15, 16];
#  - [2, 3, 5, 6] => [12, 15]

def task_02(our_list = [2, 3, 4, 5, 6]):
    result = [our_list[i] * our_list[len(our_list) - 1 - i] for i in range(math.ceil(len(our_list)/2))]
    print(result)
task_02()


# ## 3.	Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#  - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def task_03(our_list = [1.1, 1.2, 3.1, 5, 10.01]):
    '''Как я понял по условию задачи мы не считаем 0 у целого числа как дробную часть,
    поэтому сделал вариант исключающий целые числа, закоментирован вариант где 0 соответствует условию'''
    our_list = [round(x - int(x), 3) for x in our_list if x - int(x) != 0]
    #our_list = [round(x - int(x), 3) for x in our_list]
    print(max(our_list) - min(our_list))
task_03()


# ## 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#  - 45 -> 101101
#  - 3 -> 11
#  - 2 -> 10

def task_04(num):
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    print(binary)

task_04(45)


# ## 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/Негафибоначчи#:~:text=В математике%2C числа негафибоначчи — отрицательно индексированные элементы последовательности чисел Фибоначчи.)

def fiba_whith_neg(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    elif n < 0:
        return fiba_whith_neg(n+2)-fiba_whith_neg(n+1)
    elif n in (1, 2):
        return 1
    else:
        return fiba_whith_neg(n - 1) + fiba_whith_neg(n - 2)

result = []
for i in range(-8, 9):
    result.append(fiba_whith_neg(i))
print(result)

