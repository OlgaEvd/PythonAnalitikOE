#Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# num = int(input("Введите число: "))
# i = 2 
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

#Вариант2
n = int(input("Введите число: "))
def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

print (primfacs(n))