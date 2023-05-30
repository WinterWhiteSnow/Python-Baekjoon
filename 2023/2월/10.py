import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16236
# from collections import deque
# n = one()
# index_list = deque()
# y_index,x_index = 0,0
# n_list = []
# cnt = 0
# for y in range(n):
#     nn_list = list(wow())
#     for x in range(n):
#         if nn_list[x] == 9:
#             y_index,x_index=y,x
#             nn_list[x]=0
#     n_list.append(nn_list)
# index_list.append((y_index,x_index))
# state = 2
# eat = 0
# time = 0
# time_list = deque()
# move = [(-1,0),(0,-1),(1,0),(0,1)]
# def go(y,x):
#     global n
#     global state
#     global y_index,x_index
#     visited = [[False]*n for _ in range(n)]
#     q = deque()
#     q.append((y,x))
#     visited[y][x]=True
#     eat_list = []
#     d=0
#     while q:
#         temp_list = q
#         new_list = deque()
#         d+=1
#         while temp_list:
#             y,x = temp_list.popleft()
#             for i in range(4):
#                 yy,xx = y+move[i][0],x+move[i][1]
#                 if 0<=yy<=n-1 and 0<=xx<=n-1:
#                     if n_list[yy][xx] <= state:
#                         if visited[yy][xx] == False:
#                             visited[yy][xx]= True
#                             new_list.append((yy,xx))
#                     if n_list[yy][xx] != 0:
#                         if n_list[yy][xx]< state:
#                             eat_list.append((d,yy,xx))
#         if new_list:
#             q = new_list
#     # for i in distance:
#     #     print(*i)
#     # exit()
#     eat_list.sort(key=lambda x: (x[0],x[1],x[2]))
#     # print(eat_list)
#     if eat_list:
#         return eat_list
#     else:
#         return False
            
# while True:
#     a = go(y_index,x_index)
#     # print("start!!!",y_index,x_index,state,time)
#     # for i in n_list:
#     #     print(*i)
#     if type(a) == list:
#         d,yy,xx = a[0]
#         time+=d
#         y_index,x_index=yy,xx
#         n_list[y_index][x_index]=0
#         eat+=1
#         if eat == state:
#             state+=1
#             eat=0
#     else:
#         break
# print(time)


    
















