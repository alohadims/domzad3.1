from random import randint
sum = 0
numbers = []
for i in range(5):
    numbers.append(randint(-10, 10))
print(f'Заданный список: {numbers}')
for i in range(1, len(numbers), 2):
    sum += numbers[i]
print(f"Cумма чисел на нечётных позициях: {sum} ")