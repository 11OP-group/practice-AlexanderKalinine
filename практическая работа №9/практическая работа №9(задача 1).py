numb = int(input("ввидите натуральное число: "))
n = 0
while n != numb:
    n = n + 1
    if 5 <= n <= 9:
        continue
    elif 17 <= n <= 37:
        continue
    elif 78 <= n <= 87:
        continue
    print(n)