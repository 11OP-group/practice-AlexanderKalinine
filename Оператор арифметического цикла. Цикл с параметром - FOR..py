from math import *

for x in range(2, 21, 2):
    print(x)

numb_n = int(input('ввидите число факториал которого хотите узнать: '))
result = factorial(numb_n)
print(f'{numb_n}! = {result}')

numb_m = int(input('ввидите число : '))
numb_g = int(input('ввидите число : '))

if numb_m < numb_g :
    for i in range (numb_m, numb_g + 1):
        print(i)
else:
    for i in range (numb_m, numb_g - 1, -1):
        print(i)

numb_f = int(input('ввидите число : '))
numb_j = int(input('ввидите число (число должно быть больше или равно предыдущиму): '))

for num in range(numb_f, numb_j + 1):
    if (num%17 == 0) or (num%10 == 9) or (num%5 == 0 and num%3 == 0):
        print(num)