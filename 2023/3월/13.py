import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14442
# r,c,k = wow()
# if r==c==1:
#     print(1)
# else:
#     n_list = [list(map(int,list(inputing()))) for _ in range(r)]
#     visit = [[[False]*(c) for _ in range(r)] for _ in range(k+1)]
#     move_x = [0,0,1,-1]
#     move_y = [1,-1,0,0]
#     def bfs():
#         q = deque()
#         q.append((k,0,0))
#         visit[k][0][0]=1
#         while q:
#             state,y,x= q.popleft()
#             if y == r-1 and x == c-1:
#                 print(visit[state][y][x])
#                 return
#             index = visit[state][y][x]
#             for i in range(4):
#                 yyy,xxx = move_y[i]+y,move_x[i]+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if n_list[yyy][xxx] and visit[state-1][yyy][xxx] == False and state>0:
#                         visit[state-1][yyy][xxx]=index+1
#                         q.append((state-1,yyy,xxx))
#                     if n_list[yyy][xxx]== 0 and visit[state][yyy][xxx] == False:
#                         visit[state][yyy][xxx]=index+1
#                         q.append((state,yyy,xxx))
#         print(-1)
#     bfs()















