import math

x = int(input())
num_1 = x//1000
num_2 = (x//100)%10
num_3 = (x//10)%10
num_4 = x % 10

print('первая цыфра:', num_1)
print('вторая цыфра:', num_2)
print('третья цыфра:', num_3)
print('четвертая цыфра:', num_4)