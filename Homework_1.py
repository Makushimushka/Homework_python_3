#1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#Пример:
#	6 -> да
#	7 -> да
#	1 -> нет
import math


def is_weekend():

    day = int(input("Введите номер дня недели: "))

    days = list(range(1,8))
    weekend = days[5:]
    if day in weekend:
        print("выходной")
    elif day in days:
        print("не выходной")
    else:
        print("Error! Enter a correct day number ")

is_weekend()


# 2.	Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def conditions(x, y, z):
    condit = not(x or y or z) == (not x and not y and not z)

    if condit:

        return True
    else:
        return False

def rezult_task():
    values = [0, 1]
    result = []
    index = 1
    for x in values:
        for y in values:
            for z in values:
                if conditions(x, y, z):
                    result.append(f"{index}. возможно для: X:{x} Y:{y} Z:{z}")
                    index += 1
    for i in result:
        print(i)


rezult_task()




#3.	Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
#Пример:
#	x=34; y=-30 -> 4
#	x=2; y=4-> 1
#	x=-34; y=-30 -> 3

def task_3():

    flag = True
    while flag:
        x = int(input("Enter x: ").replace(' ', ''))
        y = int(input("Enter y: ").replace(' ', ''))
        if x == 0 or y == 0:
            print("X and Y must not be equal to 0")
        else:
            flag = False

    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)

task_3()


# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def task_4():
    quarter_number = int(input("Введите номер четверти: "))

    if quarter_number == 1:
        print("x > 0 and y > 0")
    elif quarter_number == 2:
        print("x < 0 and y > 0")
    elif quarter_number == 3:
        print("x < 0 and y < 0")
    elif quarter_number == 4:
        print("x > 0 and y < 0")
    else:
        print("Введите корректные данные ")

task_4()


# 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# 	A (3,6); B (2,1) -> 5,09
# 	A (7,-5); B (1,-1) -> 7,21

def task_5():
    points = ["x_1", "y_1", "x_2", "y_2"]
    values = []
    for i in points:
        try:
            values.append(int(input(f"Enter {i}: ").replace(' ', '')))
        except:
            print("Введите корректные данные")

    result = math.sqrt(((values[2] - values[0])**2 + (values[3] - values[1])**2))
    print(round(result,2))

task_5()
