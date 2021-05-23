# Задание 3.04
# Ввести строку. Вывести на экран букву, которая находится в середине этой
# строки.
# Также, если эта центральная буква равна первой букве в строке, то создать и
# вывести часть строки между первым и последним символами исходной строки.
# (подсказка: для получения центральной буквы, найдите длину строки и разделите
# ее пополам. Для создания результирующий строки используйте срез)

s = input("Your input: ")

mid_char = s[len(s) // 2]
print(f"The letter in the middle of the line: '{mid_char}'")

if mid_char == s[0]:
    new_s = s[1: -1]
    print(f"Slice of your string between the first and the last characters: '{new_s}'")