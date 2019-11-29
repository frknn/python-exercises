#find the max given number

a = int(input("ilk sayi: "))
b = int(input("ikinci sayi: "))
c = int(input("ucuncu sayi: "))

list = [a,b,c]

#with for

max = list[0]
for i in list:
    if(i>max):
        max=i
print("en buyuk sayi: ", max)


#with while

# i=1
# while i < len(list):
#     if(list[i]>max):
#         max=list[i]
#     i += 1
#
# print("en buyuk sayi: ", max)
