"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


from operator import truediv, mul, add, sub


def calc(num_1, num_2, operator):
    try:
        return f'Результат равен: {operator(num_1, num_2)}'
    except ZeroDivisionError:
        return 'Деление на 0 недопустимо.'


def calculator():
    operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operator == '0':
        return print('exit')

    if operator in operators.keys():
        try:
            number_1 = int(input('Введите первое число: '))
            number_2 = int(input('Введите второе число: '))
            print(calc(number_1, number_2, operators[operator]))
            return calculator()
        except ValueError:
            print('Вы ввели строку вместо чисел')
            return calculator()
    else:
        print('Вы ввели неверный оператор.')
        return calculator()


operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

calculator()
