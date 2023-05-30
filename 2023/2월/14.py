import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15683
# from collections import deque
# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# move1 = [(0,1)]
# move2 = [(0,-1),(0,1)]
# move3 = [(0,1),(-1,0)]
# move4 = [(0,1),(-1,0),(0,-1)]
# move5 = [(0,1),(-1,0),(0,-1),(1,0)]
# move_list = [move1,move2,move3,move4,move5]
# index_list = []
# visited = [[False]*l for _ in range(r)]
# for y in range(r):
#     for x in range(l):
#         z = n_list[y][x]
#         if z != 0 and z != 6:
#             index_list.append((y,x))
#         else:
#             if z == 6:
#                 visited[y][x]=True
# for i in index_list:
#     y,x = i
#     visited[y][x]=True
# cnt = 1000001
# def go(index_list,index,visited):
#     global r,l
#     global cnt
#     # print("Start!!!")
#     # for i in visited:
#     #     print(*i)
#     if index ==len(index_list):
#         count = 0
#         for y in range(r):
#             for x in range(l):
#                 if visited[y][x]==False:
#                     count+=1
#         if cnt > count:
#             cnt = count
#         # print("wow!")
#         # for i in visited:
#         #     print(*i)
#         return
#     for i in range(6):
#         visit = []
#         for a in visited:
#             c = []
#             for b in a:
#                 c.append(b)
#             visit.append(c)
#         # print(index,index_list,index_list[index])
#         y,x = index_list[index]
#         ind = n_list[y][x]
#         move_index = move_list[ind-1]
#         new_index = []
#         for move_y,move_x in move_index:
#             if i == 1:
#                 move_x,move_y = move_y,move_x
#             elif i == 2:
#                 move_x = move_x*(-1)
#                 move_y = move_y
#             elif i == 3:
#                 move_x,move_y = move_y,move_x
#                 move_x = move_x*(-1)
#                 move_y = move_y
#             elif i == 4:
#                 move_x,move_y = move_y,move_x
#                 move_x = move_x
#                 move_y = move_y*(-1)
#             elif i == 5:
#                 move_x = move_x
#                 move_y = move_y*(-1)
#             new_index.append((move_y,move_x))
#         # print("move!@!!",move_index,new_index)
#         q = deque()
#         for move in new_index:
#             q.append((y,x))
#             move_y,move_x = move
#             # print("move",move_y,move_x,y,x)
#             # print("Start!!!",q,move_y,move_x)
#             while q:
#                 yy,xx = q.popleft()
#                 yyy,xxx = yy+move_y,xx+move_x
#                 # print("yy,xx",yy,xx)
#                 if 0<=yyy<= r-1 and 0<=xxx<=l-1:
#                     # if visit[yyy][xxx]==False:
#                     #     visit[yyy][xxx]=True
#                     #     q.append((yyy,xxx))
#                     # else:
#                         if n_list[yyy][xxx] != 6:
#                             visit[yyy][xxx]=True
#                             q.append((yyy,xxx))
#                         else:
#                             break
#                 else:
#                     break
#                 # print("q",q)
#         index+=1
#         go(index_list,index,visit)
#         index-=1
# go(index_list,0,visited)
# print(cnt)       






