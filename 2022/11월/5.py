import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9612
# n_dict = {}
# repeat = 0
# state = "none"
# for _ in range(one()):
#     a = inputing()
#     if a not in n_dict:
#         n_dict[a]=1
#     else:
#         n_dict[a]+=1
#     if repeat == 0:
#         repeat=1
#         state = a
#     else:
#         if n_dict[a] >= repeat:
#             if n_dict[a] == repeat:
#                 state = sorted([a,state])[-1]
#             else:
#                 repeat = n_dict[a]
#                 state = a
# print(state,repeat)

#https://www.acmicpc.net/problem/1487
# n_dict = {}
# list_list = []
# for _ in range(one()):
#     a,b = wow()
#     if a-b > 0:
#         list_list.append([a,b])
# list_list = sorted(list_list,key=lambda x : x[0])
# # print(list_list)
# if len(list_list) == 0:
#     print(0)
# else:
#     state = "none"
#     profit = 0
#     for a in range(len(list_list)):
#         standard = list_list[a]
#         price = standard[0]
#         total = 0
#         for b in range(a,len(list_list)):
#             p,d = list_list[b]
#             if price-d > 0:
#                 total+=price-d
#         if state == "none":
#             state = price
#             profit = total
#         else:
#             if profit < total:
#                 state = price
#                 profit = total
#         # print(state,profit)
#     print(state)

#https://www.acmicpc.net/problem/25426
# r = one()
# n_list = []
# for _ in range(r):
#     n_list.append(list(wow()))
# n_list.sort(key=lambda x : x[1],reverse=True)
# n_list.sort(key=lambda x: x[0],reverse=True) 
# cnt = 0
# for i in n_list:
#     a,b = i
#     cnt+=a*r+b
#     r-=1
# print(cnt)

#https://www.acmicpc.net/problem/1980
# a,b,t = wow()
# if a>b:
#     a,b = b,a
# x,y = t//a,t%a
# cnt = x
# n_list = []
# for a_index in range(x+1):
#     for b_index in range(x-a_index+1):
#         if t-(a*a_index+b*b_index) >= 0 :
#             n_list.append([a_index+b_index,t-(a*a_index+b*b_index)])
            
# n_list.sort(key=lambda x: x[0],reverse=True)
# n_list.sort(key=lambda x: x[1])
# print(*n_list[0])

#https://www.acmicpc.net/problem/10774
# r = one()
# n = one()
# n_dict = {}
# for i in range(1,1+r):
#     a = inputing()
#     if i not in n_dict:
#         n_dict[i]=[a]
#     else:
#         n_dict[i]+=[a]
# # print(n_dict)
# cnt=0
# key = ["S","M","L"]
# for _ in range(n):
#     a,b = inputing().split()
#     b = int(b)
#     if b in n_dict:
#         list_list = n_dict[b]
#         k = key.index(a)
#         while k != len(key):
#             if key[k] in list_list:
#                 cnt+=1
#                 del list_list[list_list.index(key[k])]
#                 n_dict[b]=list_list
#                 break
#             else:
#                 k+=1
# print(cnt)

#https://www.acmicpc.net/problem/25379
# l = one()
# n_list = list(wow())
# n_list = [i%2 for i in n_list]
# if l == 1:
#     print(0)
# else:
#     l_cnt = 0
#     r_cnt = 0
#     l_index = 0
#     r_index = l-1
#     for i in range(l):
#         if n_list[i] == 0:
#             l_cnt+=i-l_index
#             l_index+=1
#             r_cnt+=r_index-i
#             r_index-=1
#     print(min(l_cnt,r_cnt))

print(1-((1-0.638)**7))












