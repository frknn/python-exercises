#fibonacci

# def fib(x):
#     if x == 0:
#         return 0
#     if x == 1:
#         return 1
#     return fib(x-1) + fib(x-2)
#
#
# print(fib(7))


#perfect number

# def isPerfect(x):
#     toplam = 0
#     for i in range(1, x):
#         if x % i == 0:
#             toplam += i
#     if toplam == x:
#         print("Mükemmel sayı!")
#     else:
#         print("Mükemmel sayı değil!")
#
# isPerfect(28)


#Armstrong number

# def isArmstrong(x):
#     sum = 0
#     digit = len(str(x))
#     digitlist = list(str(x))
#     for i in digitlist:
#         sum += int(i) ** digit
#     if sum == x: print("Armstrong!")
#     else: print("Not Armstrong!")
#
# isArmstrong(371)