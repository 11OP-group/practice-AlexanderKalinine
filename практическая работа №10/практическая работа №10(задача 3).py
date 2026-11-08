record_max = 0
while True:
    record = int(input("ввидите число для выхода ввидите 0: "))
    if record > record_max:
        record_max = record

    if record == 0:
        print(record_max)
        break