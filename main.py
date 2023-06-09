# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# count = int(input('Введите колличество элементов: '))
# list_count = list((map(int, input('Введите элементы списка через пробел: ').split())))
# num = int(input('Введите число: '))
# num_count = 0 
# for i in range(count):
#     if list_count[i] == num:
#         num_count += 1
# print(f'Число {num} встречается в списке А {num_count} раз.')



# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# import random

# N = int(input("Введите количество элементов в массиве "))
# list = [random.randint(1, 20) for i in range(N)]
# print(list)
# x = int(input("Введите искомое число "))
# index_element = 0
# min_element = abs(x - list[0])
# for i in range(1, N):
#     buffer_element = abs(x -list[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = list[i]

# print(f"Самый близкий по величине элемент к заданному числу {index_element}")


