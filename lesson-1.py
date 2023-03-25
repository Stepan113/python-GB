import time

# Задание 1

try:
    name=input("Введите Ваше имя: ")
    password=input("Ведите ваш пароль: ")
    age=int(input("Введите ваш возраст: "))
    print(f"Ваши данные для входа в аккаунт: имя-{name},пароль-{password},возраст-{age}")
except ValueError:
    print("Неверно введены данные")

# Задание 2

try:
    sec=int(input("Введите время в секундах: "))
    time_for=time.strftime("%H:%M:%S", time.gmtime(sec))
    print(f"Время: {time_for}")
except ValueError:
    print("Неверно введены данные")

# Задание 3

try:
    n=int(input("Введите число: "))
    if n<=0:
        print("Число меньше 0")
    else:
        n_2=n*2
        n_3=n*3
        print(f"{n}{n_2}{n_3}")
except ValueError:
    print("Неверно введены данные")

# Задание 4

try:
    revenue=int(input("Введите выручку фирмы: "))
    costs=int(input("Введите издержки фирмы: "))
    profit=revenue-costs
    print(f"Финансовый результат - прибыль. Ее величина: {profit}\nРентабельность выручки = {profit/revenue}") if revenue>=costs else print(f"Финансовый результат - убыток. Ее величина: {abs(costs-revenue)}")
    kol=int(input("Введите численность сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {profit/kol}")
except ValueError:
    print("Неверно введены данные")