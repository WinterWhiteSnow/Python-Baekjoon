import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/11967
# n,m = wow()
# light = [[False]*n for _ in range(n)]
# total = [[[] for _ in range(n)] for _ in range(n)]
# cnt = 1
# light[0][0]=True
# for _ in range(m):
#     a,b,c,d = wow()
#     a,b,c,d = a-1,b-1,c-1,d-1
#     total[a][b]+=[(c,d)]

# move = [(1,0),(0,1),(-1,0),(0,-1)]

# def bfs():
#     global n,cnt
#     q = deque()
#     q.append((0,0))
#     while q:
#         start = deque(i for i in q)
#         temp_list = deque(i for i in q)
#         visit = [[False]*n for _ in range(n)]
#         for y,x in start:
#             visit[y][x]=True
#             light_list = total[y][x]
#             for y_index,x_index in light_list:
#                 if light[y_index][x_index] == False:
#                     light[y_index][x_index]=True
#                     cnt+=1
#         while q:
#             y,x = q.popleft()
#             for yy,xx in move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<n and 0<=xxx<n:
#                     if light[yyy][xxx]:
#                         if visit[yyy][xxx]==False:
#                             temp_list.append((yyy,xxx))
#                             visit[yyy][xxx]=True

#         if start != temp_list:
#             q = temp_list
#     print(cnt)
# bfs()            

















