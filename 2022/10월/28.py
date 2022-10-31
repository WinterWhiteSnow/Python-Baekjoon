import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10546
# r = one()
# n_dict = {}
# for _ in range(r):
#     a = inputing()
#     if a not in n_dict:
#         n_dict[a]=1
#     else:
#         n_dict[a]+=1
# for _ in range(r-1):
#     n_dict[inputing()]+=1
# list_list = [a for a,b in n_dict.items() if b%2]
# print(*list_list)

#https://www.acmicpc.net/problem/9417
# import math
# for _ in range(one()):
#     n_list = list(wow())
#     n_list.sort()
#     max_max = 1
#     for i in range(len(n_list)):
#         for a in range(len(n_list)):
#             if a != i:
#                 max_max=max(max_max,math.gcd(n_list[i],n_list[a]))
#     print(max_max)

#https://www.acmicpc.net/problem/16499
# n_list = ["".join(sorted(list(inputing()))) for _ in range(one())]
# n_dict = {}
# for i in n_list:
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
# print(len(n_dict))

#https://www.acmicpc.net/problem/17419
# l = one()
# num = inputing()
# print(num.count("1"))

#https://www.acmicpc.net/problem/9575
# for _ in range(one()):
#     a_l=one()
#     a_list = set(wow())
#     b_l=one()
#     b_list = set(wow())
#     c_l=one()
#     c_list = set(wow())
#     n_dict = {}
#     for a in a_list:
#         for b in b_list:
#             for c in c_list:
#                 if {"5","8"} | set(list(str(a+b+c))) == {"5","8"}:
#                     n_dict[a+b+c]=1
#     print(len(n_dict))

#https://www.acmicpc.net/problem/24499
# l,k = wow()
# n_list = list(wow())
# n_list+=n_list
# max_max = [sum(n_list[:k])]
# for i in range(k,l+k-1):
#     max_max.append(max_max[-1]-n_list[i-k]+n_list[i])
# print(max(max_max))






        



