#Задача3
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#Вариант1
# list1 = [1.1, 1.2, 3.1, 5, 10.01]
# list2 = []
# for i in range(len(list1)):
#     a = round(list1[i]*10%10,2)
#     if a>0:
#         list2.append(a)
# b= round (float(max(list2)-min(list2))*10/100,2)
# print(b)

#Вариант2
list = [1.1, 1.2, 3.1, 5, 10.01]
mix_list = []


for i in list:
    mix_list.append(round (i-int(i), len(list)))

print(list, end = " ")
print(max(mix_list)-min(mix_list))