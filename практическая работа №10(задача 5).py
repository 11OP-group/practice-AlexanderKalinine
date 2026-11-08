balans = int(input("Ввидите свой баланс:"))
while True:
    print("Выберете команду")
    print("1. Вывести текущий баланс")
    print("2. снять 100 рублей")
    print("3. положить 100 рублей")
    print("4. Выход")
    deyctvie = int(input("Выберете действие: "))

    if deyctvie == 1:
        print(f"Текущий баланс: {balans}")
    elif deyctvie == 2:
        balans -= 100
    elif deyctvie == 3:
        balans += 100
    elif deyctvie == 4:
        break
    else:
        print("Неверная команда")