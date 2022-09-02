#1
def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')
#2
result_list = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)

#3
list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапазоне [20..240): ", list)

#4
my_list = [4, 7, 6, 4, 9, 1, 7, 1, 5, 3]
print("Исходные элементы списка:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)
#5
from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, list))
#6
#a
from itertools import count

print("<<Бесконечный итератор целых чисел, начиная с указанного>>")
n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')

#b
from itertools import cycle

list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
for i in cycle(list):
    print(i, end=' ')
#7
from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<Программа вычисления факториала числа>>")
for el in factorial_gen(15):
    print(el)