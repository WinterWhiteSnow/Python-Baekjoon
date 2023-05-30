import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/13913
# from collections import deque
# n_dict = {}
# a,b = wow()
# total = [False]*max(a*2,b*2,100001)
# path = [False]*max(a*2,b*2,100001)
# # if a>b:
# #     print(a-b)
# #     print(*[i for i in range(b,a+1)][::-1])
# # else:
# move = deque()
# move.append(a)
# total[a]=1
# path[a]=str(a)
# while move:
#     state= move.popleft()
#     move_list = path[state]
#     index = total[state]
#     x,y,z = state+1,state-1,state*2
#     if x<=100000:
#         if total[x]== False:
#             total[x]=index+1
#             path[x]=state
#             move.append(x)
#         elif total[x]>index+1:
#             total[x]=index+1
#             path[x]=state
#             move.append(x)
            
#     if y>=0:
#         if total[y]== False:
#             total[y]=index+1
#             path[y]=state
#             move.append(y)
#         if total[y]>index+1:
#             total[y]=index+1
#             path[y]=state
#             move.append(y)
            
#     if z<=100000:
#         if total[z]== False:
#             total[z]=index+1
#             path[z]=state
#             move.append(z)
#         if total[z]>index+1:
#             total[z]=index+1
#             path[z]=state
#             move.append(z)         
#     if total[b] != False:
#         break
# print(total[b]-1)
# # print(a,end=" ")
# x = b
# index_index = [b]
# for i in range(total[b]-1):
#     index_index.append(path[x])
#     x = path[x]
# print(*index_index[::-1])
    













