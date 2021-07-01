"""Задание 14.03
Создать скрипт, который при запуске принимает неопределенное количество аргументов
и считает сумму тех из них, что являются цифрами.

Пример:

python test.py 1 2 3 4 a b 5 6

--> 21
"""
import sys
print(sys.argv)

res = 0
for param in sys.argv:
    if param.isdigit():
        res += int(param)

print(res)
