def calculate_rectangle_area(a, b):
    '''умножает длинну прамоугольника на ширину'''
    S = a*b
    return S

def calculate_circle_area(R):
    '''перемножает квадрата радиуса круга на пи'''
    п = 3.14
    Sкв = п * (int(R)**2)
    return Sкв

a, b = map(int, input('Ввидите ширину и высоту прямоугольника (через пробел): ' ).split())
rectangle_area = calculate_rectangle_area(a, b)
circle_parameters = input('Ввидите радиус круга: ' )
circle_area = calculate_circle_area(circle_parameters)
print(f'площадь прямоугольника: {rectangle_area}')
print(f'площадь круга: {circle_area}')
