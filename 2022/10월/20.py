import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9322
# for _ in range(one()):
#     l = one()
#     a_list = inputing().split()
#     b_list = inputing().split()
#     str_str = inputing().split()
#     n_dict = {}
#     for i in range(l):
#         key = a_list[i]
#         index = b_list.index(key)
#         n_dict[i]=index
#     list_list = list(n_dict.items())
#     list_list = [[b,a]for a,b in list_list]
#     list_list.sort(key=lambda x: x[1])
#     for a,b in list_list:
#         print(str_str[a],end=" ")
#     print()

#https://www.acmicpc.net/problem/11292
# while True:
#     r = one()
#     if r == 0:
#         break
#     n_list = [inputing().split()+[i] for i in range(r)]
#     n_list = [[a,float(b),c] for a,b,c in n_list]
#     n_list.sort(key=lambda x: x[2])
#     n_list.sort(key=lambda x: x[1],reverse=True)
#     max_max = n_list[0][1]
#     n_list = [[a,c] for a,b,c in n_list if b==max_max]
#     n_list.sort(key=lambda x: x[1])
#     n_list = [a for a,b in n_list]
#     print(*n_list)

#https://www.acmicpc.net/problem/18311
# l,num = wow()
# n_list = list(wow())
# m_list = [n_list[0]]
# for i in range(1,l):
#     m_list.append(m_list[-1]+n_list[i])
# mm_list = [m_list[-1]]
# for i in range(l):
#     mm_list.append(mm_list[-1]+n_list[-(i+1)])
# new_list = m_list+mm_list[1:]
# num = num%new_list[-1]
# list_list = [i for i in range(1,l+1)]
# list_list = list_list+list_list[::-1]
# # print(new_list)
# # print(list_list)
# index = "none"
# for i in range(len(new_list)):
#     if new_list[i]<=num:
#         index=i
#     # print(index)
# if index == "none":
#     print(1)
# else:
#     # print(index,list_list[index])
#     if new_list[index] <= num:
#         index+=1
#     print(list_list[(index)%len(list_list)])

#https://www.acmicpc.net/problem/12033
# index = 1
# for _ in range(one()):
#     l = one()
#     list_list = list(wow())
#     wow_list = list_list
#     n_list = []
#     for i in list_list:
#         if i%4 != 0:
#             n_list.append(i)
#             del wow_list[wow_list.index((i/0.75))]
#         elif i%4 == 0 and i/0.75 in wow_list:
#             n_list.append(i)
#             del wow_list[wow_list.index((i/0.75))]
#         # print(i,i%4,i/0.75)
#     print(f"Case #{index}:",*n_list)
#     index+=1

#https://www.acmicpc.net/problem/25785
# str_str = "aeiou"
# n = list(inputing())
# if n[0] in str_str:
#     start = 1#모음
# else:
#     start = 0#자음
# check = "yes"
# for i in n[1:]:
#     if i in str_str: #예비1
#         if start == 1:
#             check = "no"
#             break
#         else:
#             start = 1
#     else:
#         if start == 0:
#             check = "no"
#             break
#         else:
#             start = 0
# print(1 if check == "yes" else "0")

#https://www.acmicpc.net/problem/15235
# l = one()
# list_list = list(wow())
# str_str = []
# while max(list_list) != 0:
#     for i in range(len(list_list)):
#         if list_list[i] != 0:
#             str_str.append(i+1)
#             list_list[i]-=1
# n_dict= {}
# for i in range(len(str_str)):
#     n_dict[str_str[i]]=i+1
# print(*(n_dict.values()))









    




