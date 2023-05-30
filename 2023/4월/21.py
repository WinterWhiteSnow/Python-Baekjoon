import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/6109
# total,k = wow()
# n_list = [one() for _ in range(k)]
# n_list.sort(reverse=True)
# zero_list = [[0]*(total+1) for _ in range(k+1)]
# for i in range(1,k+1):
#     num = n_list[i-1]
#     zero_list[i][num]=1
#     for w in range(num+1,total+1):
#         zero_list[i][w]+=(zero_list[i][w-num])+ zero_list[i-1][w]        
# print(zero_list[k][total])

#https://www.acmicpc.net/problem/14728
# r,total = wow()
# n_list = [list(wow()) for _ in range(r)]
# zero_list = [0]*(total+1)
# for i in range(r):
#     time,value = n_list[i]
#     for t in range(total,time-1,-1):
#         zero_list[t]=max(zero_list[t-time]+value,zero_list[t])
# print(zero_list[total])

#https://www.acmicpc.net/problem/1106
# import math
# total,r = wow() #모집인원수에 비용 최소
# zero_list =[-1]*(total+1)
# #index = 사람수 zero_list[index]=비용
# for _ in range(r):
#     price,person = wow()
#     repeat = math.ceil(total/person)
#     if person > total:
#         if zero_list[total] == -1:
#             zero_list[total]=price
#         else:
#             zero_list[total]=min(price,zero_list[total])
#     else:
#         if zero_list[person] == -1:
#             zero_list[person] = price
#         else:
#             zero_list[person]=min(zero_list[person],price)
#         for w in range(person+1,person*repeat+1):
#             # print(person,w,w-person,zero_list[w-person],price)
#             if w <= total:
#                 if zero_list[w]==-1:
#                     if zero_list[w-person] != -1:
#                         zero_list[w]=zero_list[w-person]+price
#                     else:
#                         zero_list[w]=price*math.ceil(w/person)
#                 else:
#                     if zero_list[w-person] != -1:
#                         zero_list[w]=min(zero_list[w],zero_list[w-person]+price)
#             else:
#                 if zero_list[w-person] != -1:
#                     zero_list[total] = min(zero_list[total],zero_list[w-person]+price)
# print(zero_list[total])






















