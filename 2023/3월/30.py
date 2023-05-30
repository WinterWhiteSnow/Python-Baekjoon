import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1937
# sys.setrecursionlimit(10**7)
# r = one()    
# n_list = [list(wow()) for _ in range(r)]
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# def bfs(y,x):
#     global r
#     if visit[y][x] == -1:
#         visit[y][x]=0
#         index = n_list[y][x]
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<r:
#                 index2 = n_list[yyy][xxx]
#                 if index<index2:
#                     visit[y][x]=max(visit[y][x],bfs(yyy,xxx))
#     return visit[y][x]+1
# visit = [[-1]*r for _ in range(r)]
# max_max = 1
# for y in range(r):
#     for x in range(r):
#         max_max = max(max_max,bfs(y,x))
# print(max_max)

#https://www.acmicpc.net/problem/17427
# n = one()
# cnt = 0
# for i in range(1,n+1):
#     cnt+=(n//i)*i
#     # print(i,cnt)
# print(cnt)

l = one()
n_list = list(wow())
print(sorted(n_list))




















