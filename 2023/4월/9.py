import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3067
# for _ in range(one()):
#     l = one()
#     n_list = [0]+list(wow())
#     k = one()
#     while len(n_list) > 0 and n_list[-1] > k:
#         n_list.pop()
#     l = len(n_list)
#     list_list = [0]*(k+1)
#     for index in range(1,l):
#         # print("Start!",index,l)
#         num = n_list[index]
#         list_list[num]+=1
#         for cost in range(num+1,k+1):
#             list_list[cost]+=list_list[cost-num]
#     print(list_list[k])

#https://www.acmicpc.net/problem/17845
# limit,k = wow()
# n_list = [[0,0]]+[list(wow()) for _ in range(k)]
# n_list.sort(key=lambda x: x[1])
# while len(n_list)>0 and n_list[-1][1] > limit:
#     n_list.pop()
# k = len(n_list)
# total = [[0]*(limit+1) for _ in range(k)]
# if k == 1:
#     print(0)
# else:
#     for index in range(1,k):
#         value,time = n_list[index]
#         total[index][time]=value
#         for t in range(1,limit+1):
#             if t < time:
#                 total[index][t]=total[index-1][t]
#             else:
#                 total[index][t]=max(total[index-1][t],total[index-1][t-time]+value)
#     print(total[-1][limit])

#https://www.acmicpc.net/problem/22115
# l,k = wow()
# n_list = [0]+list(wow())
# n_list.sort()
# while len(n_list)>0 and n_list[-1]>k:
#     n_list.pop()
# l = len(n_list)
# total = [[l]*(k+1) for i in range(l)]
# end = 0
# for index in range(1,l):
#     num = n_list[index]
#     total[index][num] = 1
#     for i in range(num):
#         total[index][i] = total[index-1][i]
#     for cost in range(num+1,k+1):
#         if cost < num:
#             total[index][cost] = total[index-1][cost]
#         else:
#             total[index][cost]=min(total[index-1][cost],total[index-1][cost-num]+1)
# if k == 0:
#     print(0)
# else:
#     print(total[l-1][k] if total[l-1][k] != l else -1)

#https://www.acmicpc.net/problem/6126
# r,k = wow()
# n_list = [0]
# for _ in range(r):
#     a = one()
#     if a < k:
#         n_list.append(a)
# l = len(n_list)
# total = [0]*(k+1) 
# # print(n_list,l)
# for index in range(1,l):
#     num = n_list[index]
#     total[num]+=1
#     for c in range(num+1,k+1):
#         total[c]+=total[c-num]
# print(total[k])








