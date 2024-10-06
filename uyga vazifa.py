#1

# a = int(input("a:"))
# b = int(input("b:"))
#
# even_numbers = []
#
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         even_numbers.append(i)
#
# print(even_numbers)

# even_numbers_v2 = [n for n in range(a, b + 1) if n % 2 == 0]

# print(even_numbers_v2)


#2
# a=int(input("a:"))
# b=int(input("b:"))
#
# even_numbers=[]
# for i in reversed(range(a,b+1)):
#     if i%2==1:
#         even_numbers.append(i)
#
# print(even_numbers)


#3
# list1 = ["So'z", "yana so'z", 1, 2, 3, "Bayram"]
#
# TEXT = []
# OTHER = []
#
# for item in list1:
#     if type(item) == str:
#         TEXT.append(item)
#     else:
#         OTHER.append(item)
#
# TEXT.sort()

# print(TEXT)
# print(OTHER)



# 4
# N = [1, 2, 3, 6, 8, 9, 33, 4]
# a = int(input("Son kiriting: "))
#
# found = False
# for i in range(len(N)):
#     for j in range(i+1, len(N)):
#         if N[i] + N[j] == a:
#             print(f"{N[i]} va {N[j]} sonlari yig'indisi {a} ga teng. Indekslari: {i}, {j}")



#5

# soz=input("soz kiriting : ")
#
# N=[]
#
# for i in soz.split():
#     N.append(i)
#
# sorted_list = sorted(N, key=str.lower)
#
# print(sorted_list)


# 6
# son = int(input("Son kiriting: "))
#
# c=0
# for i in range(1, son+1 ):
#     c+=i
# print("yigindisi = ",c)




# 7
# soz=input("soz kiriting : ")
#
# N=[]
#
# for i in soz.split():
#     N.append(i)
#
# for i in range(0, len(N), 2):
#     N[i] = N[i][::-1]
#
# print(N)
#



# 9
# soz = input("So'z kiriting: ")
# harf = input("Harf kiriting: ")
# soz = soz.replace(harf, harf.upper())
#
# print(soz)



#10
# son = int(input("son ni kiriting: "))
# sum = 0
# for i in range(1, son + 1):
#     n = int('2' * i)
#     sum += n
# print(f"Yig'indi: " , sum)


# 11
# son_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# tortinchisi = son_tuple[3]
# songgisi = son_tuple[5]
#
# print("4-element:", tortinchisi)
# print("So'nggi raqamdan boshlaganda <4-elementi>:",songgisi)


# 12
# my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# for i in range(len(my_list)):
#     vaqtN = list(my_list[i])
#     vaqtN[-1] = 9
#     my_list[i] = tuple(vaqtN)
#
# print(my_list)



# # 13
# mylist = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
# ochirish = list(filter(lambda item: item, mylist))
# print(ochirish)




#15
# soz = input("So'zni kiriting: ")
#
# javob = tuple(soz)
#
# print("Natija:", javob)