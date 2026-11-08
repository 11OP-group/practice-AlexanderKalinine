count = 3
number_min = 0
while True:
    number = int(input("ввидите  число :"))
    if number > number_min:
        print(number)
        number_min = number
        count -= 1
        if count == 0:
            print("последоательность принята")
            break
    else:
        print("число меньше предидущего видите число повторно")