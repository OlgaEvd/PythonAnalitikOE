# Задача5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 2

#Вариант1
# num = int(input("Введите число: "))
# list = []
# list.append(0)
# list.append(1)
# list.insert(0,-1)
# def Fibonachi(n):
#     index = -1
#     for i in range (2, n+1):
#         list.append(list[i*2-2]+list[i*2-3])
#         list.insert(0, (abs (list[0]) +abs(list[1]))*index)
#         index = index *-1
#     print(list)
# Fibonachi(num)

#Вариант2
def Fibonachi():
    num = int(input("Введите любое натуральное число: "))
    fib = []
    a,b = 1,1
    for i in range(num):
        fib.append(a)
        a,b = b, a+b
    a,b = 0,1
    for j in range(num+1):
        fib.insert(0,a)
        a,b = b, a-b
    print(f"Список чисел Фибоначи для {num}: {fib}")


Fibonachi()
