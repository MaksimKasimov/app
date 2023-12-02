

#lang = 'EN'
#lang_opt = input('Enter L to change language or other key to conrinue>> ')
prodolzhit = 'y'
while prodolzhit == 'y':
    f_num = float(input('Введите первое число>> '))
    oper = input('Введите операцию>> ')
    s_num = float(input('Введите второе число>> '))    
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print('Error')
    prodolzhit = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>> ")