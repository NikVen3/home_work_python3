
#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


# N = int(input('Введите число: '))
# i = 0
# while N >= 2**i:
#     i += 1
#     print(2**(i-1))




# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Выведите минимальное количество монет, которые нужно перевернуть



import random

from random import randint

amount_coin = int(input('введите количество монет: '))

obverse = 0
reverse = 0
coins = [0, 1]
for i in range(amount_coin):
    random.shuffle(coins)
    print(f'все монеты{coins}')
    if int(coins[0]) == 0:
        obverse += 1
    if int(coins[0]) == 1:
        reverse += 1
print('всего монет', reverse, obverse)
if reverse > obverse:
    ans = obverse
else:
    ans = reverse
print(f"минимальное количество монет, которые нужно перевернуть {ans}")


# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# S = int(input("Введите сумму чисел: "))
# P = int(input("Введите произведение чисел: "))
#
# found_solution = False
#
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if i + j == S and i * j == P:
#             print("Задуманные числа:", i, "и", j)
#             found_solution = True
#             break
#
#     if found_solution:
#         break
#
# if not found_solution:
#     print("Числа не удалось отгадать.")





