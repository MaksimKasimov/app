"""Программа калькулятор на русском языке"""
import time

print(time.ctime())
next = "y"
while next == "y":
    f_num = float(input("Введите первое число>> "))
    oper = input("Введите операцию>> ")
    s_num = float(input("Введите второе число>> "))
    if oper == "+":
        print('Результат сложения: ', f_num + s_num)
    elif oper == "-":
        print('Результат вычитания: ', f_num - s_num)
    elif oper == "*":
        print('Результат умножения: ', f_num * s_num)
    elif oper == "/":
        print('Результат деления: ', f_num / s_num)
    else:
        print("Error")
    next = input(
        "Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>> "
    )
    if next == "y":
        next = "y"
    else:
        print("Goodbay !")
