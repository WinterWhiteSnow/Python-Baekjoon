import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/25193
# import math
# l = one()
# n_list = list(inputing())
# total = n_list.count("C")
# print(math.ceil(total/(l-total+1)))

#https://www.acmicpc.net/problem/6159
# n,s = wow()
# n_list = sorted([one() for _ in range(n)])
# cnt = 0
# for a in range(n-1):
#     for b in range(a+1,n):
#         if n_list[a]+n_list[b] <=s:
#             cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/5046
# p,b,r,l = wow()
# min_min = 500001
# for _ in range(r):
#     price = one()
#     p_limit = sorted(list(wow()),reverse=True)
#     for i in p_limit:
#         if i>=p:
#             min_min=min(min_min,price*p)
#         else:
#             break
# print("stay home" if min_min > b else min_min)

#https://www.acmicpc.net/problem/11999
# n_list = sorted(list(wow()))
# a = n_list[0]
# b = n_list[1]
# max_max = 0
# for a_index in range(n_list[-1]//a+1):
#     for b_index in range(n_list[-1]//b+1):
#         if a*a_index+b*b_index <= n_list[-1]:
#             max_max=max(max_max,a*a_index+b*b_index)
# print(max_max)

#https://www.acmicpc.net/problem/14584
# import string
# str_str = list(string.ascii_lowercase)
# a = list(inputing())
# n_list = [inputing() for _ in range(one())]
# check = "no"
# for i in n_list:
#     if i in a:
#         check ="yes"
# if check =="yes":
#     print(a)
# else:
#     gap = 1
#     while check == "no":
#         for i in range(len(a)):
#             index = str_str.index(a[i])
#             a[i]=str_str[(index+1)%len(str_str)]
#         a = "".join(a)
#         for key in n_list:
#             if key in a:
#                 check = "yes"
#                 break
#         a = list(a)
#     print("".join(a))

#https://www.acmicpc.net/problem/25206
# n_dict = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
# total = 0
# cnt = 0
# for i in sys.stdin.readlines():
#     a,b,c = i.split()
#     b = float(b)
#     if c != "P":
#         total+=b
#         cnt += b*n_dict[c]
# print(cnt/total)

#https://www.acmicpc.net/problem/24228
# n,r = wow()
# print((n+1)+2*(r-1))

#https://www.acmicpc.net/problem/15702
# n,r = wow()
# n_list = list(wow())
# n_dict = {}
# for _ in range(r):
#     a_list = inputing().split()
#     cnt = 0
#     num = int(a_list[0])
#     a_list = a_list[1:]
#     for i in range(len(a_list)):
#         if a_list[i] == "O":
#             cnt+=n_list[i]
#     n_dict[num]=cnt
# x = sorted(list(n_dict.items()),key=lambda x: x[0])
# x.sort(key=lambda x: x[1],reverse=True)    
# print(*x[0])

#https://www.acmicpc.net/problem/24509
# r = one()
# n_dict = {}
# for i in range(r):
#     n_list = list(wow())
#     num = n_list[0]
#     n_list = n_list[1:]
#     for index in range(4):
#         if index not in n_dict:
#             n_dict[index]=[[n_list[index],num]]
#         else:
#             n_dict[index]+=[[n_list[index],num]]
# new_list = []
# for i in range(4):
#     list_list = n_dict[i]
#     list_list.sort(key=lambda x: x[1])
#     list_list.sort(key=lambda x: x[0],reverse=True)
#     for a,b in list_list:
#         if b not in new_list:
#             new_list.append(b)
#             break
# print(*new_list)   

#https://www.acmicpc.net/problem/11564
# k,a,b = wow()
# cnt = 0
# if b<0:
#     # print("wow!!")
#     a = abs(a)
#     b = abs(b)
#     gap = max(a,b)//k-min(a,b)//k
#     if min(a,b)%k == 0:
#         gap+=1
#     cnt+=gap
# else:
#     if a<0:
#         if a<=0<=b:
#             cnt+=1
#         cnt+=abs(a)//k
#         cnt+=b//k
#     else:
#         gap = b//k-a//k
#         if (min(a,b))%k == 0:
#             gap+=1
#         cnt+=gap
# print(cnt)

#https://www.acmicpc.net/problem/22935
# list_list = [bin(i)[2:].zfill(4) for i in range(1,16)]
# list_list+=list_list[::-1][1:-1]
# list_list = [i.replace("0","V").replace("1","딸기") for i in list_list]
# for _ in range(one()):
#     repeat = (one()-1)%len(list_list)
#     print(list_list[repeat])

#https://www.acmicpc.net/problem/18787
# l = one()
# a_list = list(inputing())
# b_list = list(inputing())
# state = "none"
# cnt = 0
# for i in range(l):
#     x = a_list[i]
#     y = b_list[i]
#     if x != y:
#         if state == "none":
#             cnt+=1
#             state = 1
#         else:
#             state+=1
#     else:
#         state = "none"
# print(cnt)









