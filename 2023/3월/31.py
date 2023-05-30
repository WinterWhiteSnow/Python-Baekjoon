import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1986
# r,c = wow()
# visit = [[0]*c for _ in range(r)]
# n_list = [list(wow()) for _ in range(3)]
# n_list = n_list[::-1]       
# q_move = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
# k_move = [(2,1),(1,2)]
# total = r*c
# k = []
# for y,x in k_move:
#     k.append((y,-x))
# k_move = k_move+k
# k = []
# for y,x in k_move:
#     k.append((-y,x))
# k_move = k_move+k
# for i in range(3):
#     a = n_list[i]
#     l,a_list = a[0],a[1:]
#     # print(l,a_list)
#     for index in range(0,2*l,2):
#         y,x = a_list[index]-1,a_list[index+1]-1
#         visit[y][x]="X"
#         total-=1
# for i in range(3):
#     a = n_list[i]
#     l,a_list = a[0],a[1:]
#     # print(l,a_list)
#     for index in range(0,2*l,2):
#         y,x = a_list[index]-1,a_list[index+1]-1
#         if i == 0:
#             continue
#         elif i == 1:
#             for yy,xx in k_move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if visit[yyy][xxx] == 0:
#                         total-=1
#                         visit[yyy][xxx]=1
#         else:
#             # print("start!",y_index,x_index)
#             for yy,xx in q_move:
#                 y_index,x_index = y,x
#                 # print("d",yy,xx)
#                 while 0<=yy+y_index<r and 0<=xx+x_index<c:
#                     y_index+=yy
#                     x_index+=xx
#                     # print("go",y_index,x_index,visit[y_index][x_index])
#                     if visit[y_index][x_index] =="X":
#                         break
#                     if visit[y_index][x_index]==0 or visit[y_index][x_index]==1:
#                         if visit[y_index][x_index] == 0:
#                             total-=1
#                         visit[y_index][x_index] = 1
# print(total)

#https://www.acmicpc.net/problem/13901
# sys.setrecursionlimit(10**7)
# r,c = wow()
# visit = [[0]*c for _ in range(r)]
# for _ in range(one()):
#     y,x = wow()
#     visit[y][x] = True
# y,x = wow()
# visit[y][x]=True
# state = 0
# move = list(wow())
# move_list = []
# for i in move:
#     if i == 1:
#         move_list.append((-1,0))
#     if i == 2:
#         move_list.append((1,0))
#     if i == 3:
#         move_list.append((0,-1))
#     if i == 4:
#         move_list.append((0,1))
# def go(y,x,d,cnt):
#     global r,c
#     if cnt == 4:
#         print(y,x)
#         return
#     yy,xx = move_list[d]
#     yyy,xxx = y+yy,xx+x
#     if 0<=yyy<r and 0<=xxx<c:
#         if visit[yyy][xxx]==0:
#             visit[yyy][xxx]=True
#             go(yyy,xxx,d,0)
#         else:
#             go(y,x,(d+1)%4,cnt+1)
#     else:
#         go(y,x,(d+1)%4,cnt+1)
# go(y,x,state,0)

#https://www.acmicpc.net/problem/11403
# r = one()
# n_dict = {}
# for i in range(r):
#     n_dict[i]=[]
# n_list = [list(wow()) for _ in range(r)]
# for k in range(r):
#     for y in range(r):
#         for x in range(r):
#             n_list[y][x] = 1 if n_list[y][k] == n_list[k][x] == 1 else n_list[y][x]
# for i in n_list:
#     print(*i)

#https://www.acmicpc.net/problem/1058
# r = one()
# n_list = [list(inputing()) for _ in range(r)]
# visit = [[0]*r for _ in range(r)]
# max_max = 0
# for k in range(r):
#     for y in range(r):
#         for x in range(r):
#             # print(y,x          ,y,k,x)
#             if y==x:
#                 continue
#             if n_list[y][x] == "Y":
#                 visit[y][x]+=1
#             else:
#                 if n_list[y][k] == n_list[k][x] == "Y":
#                     visit[y][x]+=1
# max_max = 0
# for y in range(r):
#     cnt = 0
#     for x in range(r):
#         if visit[y][x] != 0:
#             cnt+=1
#     max_max = max(max_max,cnt)
# print(max_max)












