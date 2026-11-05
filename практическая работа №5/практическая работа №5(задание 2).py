import math

weight, height = map(int, input('Ввидите вес и рост (только в назвоном порядке через пробел): ' ).split())
BMI = weight/(height * height)
print(f"Индекса Массы Тела (ИМТ): {BMI}")
