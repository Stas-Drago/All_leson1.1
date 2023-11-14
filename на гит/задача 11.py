from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(-10, 10))
print(numbers)
print('Первый элелмент списка:',numbers[0])
print('Последний элелмент списка:',numbers[-1])