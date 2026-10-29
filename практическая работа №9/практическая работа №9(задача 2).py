current_pos = 0

while True:
    name = input("ввидите имя участника: ").strip()
    if name == "Александра":
        alex_pos = current_pos
    elif name == "Левон":
        levon_pos = current_pos
    current_pos += 1
    if not name:
        break

result = levon_pos - alex_pos - 1
if result < 0:
    print("вырожение не соответствует логиике")
elif result > 0:
    print(f"между Александрой и Левонам {result}")
elif result == 0:
    print("между Александрой и Левонам нет людей")