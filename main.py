num1 = int(input('ваше первое число:'))
num2 = int(input('ваше второе число:'))
operation = input('''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
Ваш выбор:
''')
try:
    if operation == '+':
        result = num1 + num2
    if operation == '-':
        result = num1 - num2
    if operation == '/':
        result = num1 / num2
except ZeroDivisionError:
    result = "Деление на ноль запрещено"
if operation == '*':
    result = num1 * num2
    print(f"Результат: {result}")
