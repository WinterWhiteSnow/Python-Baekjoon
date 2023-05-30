import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2096
# r = one()
# total = list(wow())
# max_max = [i for i in total]
# min_min = [i for i in total]
# for _ in range(r-1):
#     a,b,c = wow()
#     max_max[0],max_max[1],max_max[2]=max(max_max[0],max_max[1])+a,max(max_max[0],max_max[1],max_max[2])+b,max(max_max[1],max_max[2])+c
#     min_min[0],min_min[1],min_min[2]=min(min_min[0],min_min[1])+a,min(min_min[1],min_min[2],min_min[0])+b,min(min_min[1],min_min[2])+c
# print(max(max_max),min(min_min))

#https://www.acmicpc.net/problem/1890
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# q = deque()
# q.append((0,0))
# cnt = 0
# visit = [[0]*r for _ in range(r)]
# visit[0][0]=1
# for y in range(r):
#     for x in range(r):
#         if y==x==r-1:
#             continue
#         if visit[y][x] != 0:
#             index = n_list[y][x]
#             value = visit[y][x]
#             if y+index<r:
#                 visit[y+index][x]+=value
#             if x+index<r:
#                 visit[y][x+index]+=value
#             # print(y,x)
#             # for i in visit:
#             #     print(*i)
# print(visit[r-1][r-1])

#https://www.acmicpc.net/problem/1520
# r,c = wow()
# n_list = [list(wow()) for _ in range(r)]
# visit = [[-1]*c for _ in range(r)]
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# visit[r-1][c-1]=1
# def bfs(y,x):
#     global r,c
#     index = n_list[y][x]
#     if y==r-1 and x==c-1:
#         return 1
#     if visit[y][x]==-1:
#         visit[y][x]=0
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 index2 = n_list[yyy][xxx]
#                 if index>index2:
#                     visit[y][x]+=bfs(yyy,xxx)
#     return visit[y][x]
# bfs(0,0)
# print(visit[0][0])

                    
















