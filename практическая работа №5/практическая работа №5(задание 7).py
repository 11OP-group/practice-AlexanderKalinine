import math

cost = 49.5

def calculator ():
    distance = float(input("какое расстояние (км)?: "))
    consumption = float(input("Сколько литров на 100 км ест машина?: "))

    total_liters = distance * (consumption / 100)
    total_cost = total_liters * cost

    print(f"Нужно бензина: {total_liters}")
    print(f"Стоимость: {total_cost}")

calculator ()