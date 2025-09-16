import math

def count_matching_numbers(a, b, c):
    # Проверяем, все ли три числа совпадают
    if a == b == c:
        return 3
    # Проверяем, совпадают ли два числа
    elif a == b or b == c or a == c:
        return 2
    # Если все числа разные
    else:
        return 0

# Пример использования:
x = int(input("Введите первое целое число: "))
y = int(input("Введите второе целое число: "))
z = int(input("Введите третье целое число: "))

result = count_matching_numbers(x, y, z)
print(result)

# Пример использования math.sin, исправлено добавлением импорта math
s = (1/2) + (math.sin(y)**2) * (1 + (z**2 / 3) - (z**2 / 5))
print(s)