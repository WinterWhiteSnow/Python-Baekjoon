import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1743
# from collections import deque
# r,c,k= wow()
# n_list = [[0]*c for _ in range(r)]
# visit = [[0]*c for _ in range(r)]
# for _ in range(k):
#     y,x = wow()
#     y-=1
#     x-=1
#     n_list[y][x]=1
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# def go(y,x):
#     q = deque()
#     visit[y][x]=1
#     q.append((y,x))
#     cnt = 1
#     while len(q) > 0:
#         y,x = q.popleft()
#         # print("start!",y,x,cnt)
#         for yy,xx in move:
#             yyy,xxx = y+yy,x+xx
#             if 0<=yyy<r and 0<=xxx<c:
#                 if visit[yyy][xxx]==0 and n_list[yyy][xxx]==1:
#                     visit[yyy][xxx]=1
#                     cnt+=1
#                     q.append((yyy,xxx))
#     return cnt
# max_max = 0
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == 1 and visit[y][x]==0:
#             max_max = max(max_max,go(y,x))
# print(max_max)
















