open = 4590
while True:
    password = int(input("Ввидите пин код: "))
    if password == open:
        print("Доступ разрешен")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")