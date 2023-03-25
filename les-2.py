# Задача 1
# import random
# n=int(input("Введите кол-во монет: "))
# monet=[random.randint(0,1) for x in range(1,n+1)]
# print(monet)
# print(f"Необходимо перевернуть {len([i for i in monet if i==1])}" if len([i for i in monet if i==1]) else f"Необходимо перевернуть {len([i for i in monet if i==0])}")
# Задача 2
# x=int(input())
# y=int(input())
# s=x+y
# p=x*y
# for i in range(1,1000):
#     for j in range(1,1000):
#         if i+j==s and i*j==p:
#             print(f"X-{i},Y-{j}")
#             break
# Задача 3
# N=int(input())
# i=0
# while True:
#     if 2**i>N:
#         break
#     print(2**i)
#     i+=1