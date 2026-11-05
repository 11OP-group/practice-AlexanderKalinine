from math import *

def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area

print("Введите координаты трёх точек (A, B, C).")

x1 = float(input("Координата X точки A: "))
y1 = float(input("Координата Y точки A: "))

x2 = float(input("Координата X точки B: "))
y2 = float(input("Координата Y точки B: "))

x3 = float(input("Координата X точки C: "))
y3 = float(input("Координата Y точки C: "))

side_ab = calculate_distance(x1, y1, x2, y2)
side_bc = calculate_distance(x2, y2, x3, y3)
side_ca = calculate_distance(x3, y3, x1, y1)

area = calculate_triangle_area(side_ab, side_bc, side_ca)

print(f"Площадь треугольника ABC: {area}")