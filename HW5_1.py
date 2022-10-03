
# ЗАДАЧА 1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# txt = input("Введите текст:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')


txt = input("Введите текст:\n")
print(f"Исходный текст: {txt}")
lst = list(filter(lambda x: not "абв" in x, txt.split()))
print(f'Результат: {" ".join(lst)}')