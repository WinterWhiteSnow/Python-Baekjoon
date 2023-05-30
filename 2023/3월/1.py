import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/20058
# from collections import deque
# m,q_l = wow()
# l = 2**m
# n_list = [list(wow()) for _ in range(l)]
# m_list = list(wow())
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# def check(y,x):
#     global l
#     cnt = 0
#     for i in move:
#         yy,xx = i
#         yyy,xxx = y+yy,x+xx
#         if 0<=yyy<l and 0<=xxx<l:
#             cnt+=visit[yyy][xxx]
#     if cnt >=3:
#         return True
#     else:
#         return False
# for ind in range(q_l):
#     index = 2**m_list[ind]
#     visit = [[True]*l for _ in range(l)]
#     for x in range(0,l,index):
#         for y in range(0,l,index):
#             list_list = []
#             for y_index in range(y,y+index):
#                 # print(n_list[y_index][x:x+index],y_index,x)
#                 list_list.append(n_list[y_index][x:x+index])
#             list_list=list_list[::-1]
#             # print(list_list)
#             for y_index in range(index):
#                 for x_index in range(index):
#                     # print(y_index,x_index,list_list[y_index][x_index])
#                     # print("x,y",x,y)
#                     n_list[x_index+y][y_index+x]=list_list[y_index][x_index]
#                     if n_list[x_index+y][y_index+x] == 0:
#                         visit[x_index+y][y_index+x]=False
#     # cnt = 0
#     total = 0
#     index_list = []
#     for y in range(l):
#         for x in range(l):
#             if not check(y,x):
#                 index_list.append((y,x))
#                 # if n_list[y][x]>=1:
#                 #     n_list[y][x]-=1
#                 #     if n_list[y][x] == 0:
#                 #         visit[y][x]=False
#             # total+=n_list[y][x]
#             # cnt+=visit[y][x]
#     for y,x in index_list:
#         if n_list[y][x]>=1:
#             n_list[y][x]-=1
#     for y in range(l):
#         for x in range(l):
#             if n_list[y][x] == 0:
#                 visit[y][x]=False
#             total+=n_list[y][x]
#             # cnt+=visit[y][x]
#     # print(m_list[ind],"now")
# cnt = 0
# # for i in n_list:
# #     print(*i)
# def bfs(y,x,visited):
#     global l
#     # v = []
#     # for vv in visited:
#     #     vi = []
#     #     for vvv in vv:
#     #         vi.append(vvv)
#     #     v.append(vi)
#     q = deque()
#     q.append((y,x))
#     cnt = 0
#     if visited[y][x] == True:
#         cnt+=1
#         visited[y][x]=False
#     while q:
#         y,x = q.popleft()
#         for yy,xx in move:
#             yyy,xxx = y+yy,xx+x
#             if 0<=yyy<l and 0<=xxx<l:
#                 if visited[yyy][xxx]:
#                     visited[yyy][xxx]=False
#                     cnt+=1
#                     q.append((yyy,xxx))
#     # print("count!!!",cnt)
#     return cnt        
# for y in range(l):
#     for x in range(l):
#         if visit[y][x]:
#             a = bfs(y,x,visit)
#             if cnt < a:
#                 cnt = a
# print(total)
# print(cnt)



