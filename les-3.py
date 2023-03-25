# Задача 1
# n=int(input("Введите номер месяца: "))
# month_list=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
# month_dict={"1":"Январь",
#             "2":'Февраль',
#             "3":"Март",
#             "4":"Апрель",
#             "5":"Май",
#             "6":"Июнь",
#             "7":"Июль",
#             "8":"Август",
#             "9":"Сентябрь",
#             "10":"Октябрь",
#             "11":"Ноябрь",
#             "12":"Декабрь"}
# print(month_dict.get(f"{n}"))
# print(month_list[n-1])
# Задача 2
# try:
#     n=int(input("Введите первое число: "))
#     x=int(input("Введите второе число: "))
#     print(n/x)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя)")

# Задача 3
# def pol_cpick(name=input("Введите ваше имя: "),fam=input("Ведите вашу фамилию: "),
#               year=int(input("Год рождения: ")),city=input("Город: "),email=input("Почта: "),number=int(input("Номер телефона: "))):
#     return f"{name} {fam} {year} года рождения,проживает в городе {city},email: {email}," \
#            f"телефон: {number}"
# print(pol_cpick())
# Задача 4
# def my_func(*args):
#     kol=[*args]
#     kol.sort()
#     print(kol[-1]+kol[-2])

# my_func(156,5,74)

# def my_func_2(*args):
#     kol=[*args]
#     max_el=max(kol)
#     kol.pop(kol.index(max_el))
#     print(max_el+max(kol))
# my_func_2(156,5,74)