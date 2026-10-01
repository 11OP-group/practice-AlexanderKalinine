import math

'''x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(distance)'''

'''x1, y1 = map(float, input('ввидите кординаты первой точки (x y через пробел): ').split())
x2, y2 = map(float, input('ввидите кординаты второй точки (x y через пробел): ').split())

distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(f'растояние между точками: {distance:.2f}')'''

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1, y1 = map(float, input('ввидите кординаты первой точки (x y через пробел): ').split())
x2, y2 = map(float, input('ввидите кординаты второй точки (x y через пробел): ').split())

print(f'растояние между точками: {distance(x1, y1, x2, y2): .f2}')
