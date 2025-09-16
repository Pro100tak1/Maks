import math

def is_leap_year(year):
    # Проверяем, является ли год високосным
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Да")
    else:
        print("Нет")

# Пример использования:
year = int(input("Введите натуральное число (год): "))

is_leap_year(year)