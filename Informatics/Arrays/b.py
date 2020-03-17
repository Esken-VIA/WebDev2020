# Дан массив, состоящий из целых чисел. Напишите программу, которая выводит те элементы массива, которые являются чётными числами.
#
# Входные данные
# Сначала задано число N — количество элементов в массиве (1N100). Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
# Необходимо вывести все четные элементы массива (то есть те элементы, которые являются четными числами).

# Примеры
# входные данные
# 5
# 1 2 3 4 5
#
# выходные данные
# 2 4

n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    if x[i] % 2 == 0:
        print(x[i])