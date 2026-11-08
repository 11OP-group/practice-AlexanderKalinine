prace_all = 0

while True:
    prace = int(input("Ввидите цену товара если товары закончились ввидите 0: "))
    if prace < 0:
        print("Ошибка цены")
    elif prace == 0:
        break
    else:
        prace_all += prace

if prace_all > 1000:
    print(prace_all*0.9)
else:
    print(prace_all)