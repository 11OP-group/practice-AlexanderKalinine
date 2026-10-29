price = int(input("ввидите цену услуги:"))
coin = 0
while price >= 25:
    price = price - 25
    coin += 1
while price >= 10:
    price = price - 10
    coin += 1
while price >= 5:
    price = price - 5
    coin += 1
while price >= 1:
    price = price - 1
    coin += 1
print(coin)