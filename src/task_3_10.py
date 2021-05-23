# Задание 3.10
# Получить на ввод количество рублей и копеек и вывести в правильной
# форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки

rub = input("Рублей: ")
kop = input("Копеек: ")

if not (rub.isdigit() or kop.isdigit()):
    print("Некорректный ввод. Рубли и копейки должны быть целыми числами.")
else:
    rub = int(rub)
    kop = int(kop)
    if kop >= 100:
        rub += kop // 100
        kop %= 100

    rk = {0: ["рублей", "копеек"],
          1: ["рубль", "копейка"],
          2: ["рубля", "копейки"],
          3: ["рубля", "копейки"],
          4: ["рубля", "копейки"],
          5: ["рублей", "копеек"],
          6: ["рублей", "копеек"],
          7: ["рублей", "копеек"],
          8: ["рублей", "копеек"],
          9: ["рублей", "копеек"]}

    if rub > 100 and rub % 100 in (11, 12, 13, 14):
        rub = str(rub) + " " + rk[0][0]
    elif rub > 20:
        rub = str(rub) + " " + rk[rub % 10][0]
    elif 20 > rub >= 10:
        rub = str(rub) + " " + rk[0][0]
    else:
        rub = str(rub) + " " + rk[rub][0]

    if kop > 20:
        kop = str(kop) + " " + rk[kop % 10][1]
    elif 20 > kop >= 10:
        kop = str(kop) + " " + rk[0][1]
    else:
        kop = str(kop) + " " + rk[kop][1]

    print(rub, kop)
