import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16933
# r,c,k = wow()
# n_list = [list(map(int,list(inputing()))) for _ in range(r)]
# visit = [[[0]*c for _ in range(r)] for _ in range(k+1)]
# time = 1
# if r==c==1:
#     if n_list[r-1][c-1]:
#         if k == 0:
#             print(-1)
#         else:
#             print(1)
#     else:
#         print(1)
# else:
#     def bfs():
#         global time
#         q = deque()
#         visit[k][0][0]=1
#         q.append((0,0,k))
#         move_y = [1,-1,0,0]
#         move_x = [0,0,1,-1]
#         while q:
#             temp_q = deque()
#             while q:
#                 y,x,state = q.popleft()
#                 index = visit[state][y][x]
#                 if y == r-1 and x == c-1:
#                     print(visit[state][y][x])
#                     return
#                 for i in range(4):
#                     yy,xx = move_y[i]+y,move_x[i]+x
#                     if 0<=yy<r and 0<=xx<c:
#                         if n_list[yy][xx]:
#                             if time:
#                                 if state-1>=0:
#                                     if visit[state-1][yy][xx] == False:
#                                         visit[state-1][yy][xx] = index+1
#                                         temp_q.append((yy,xx,state-1)) 
#                                     elif visit[state-1][yy][xx]>index+1:
#                                         visit[state-1][yy][xx] = index+1
#                                         temp_q.append((yy,xx,state-1))
#                             else:
#                                 if state-1>=0:
#                                     if visit[state-1][yy][xx] == False:
#                                         visit[state][y][x]=index+1
#                                         temp_q.append((y,x,state))                
#                         elif n_list[yy][xx] == False:
#                             if visit[state][yy][xx] == False:
#                                 visit[state][yy][xx]=index+1
#                                 temp_q.append((yy,xx,state))
#                             elif visit[state][yy][xx] > index+1:
#                                 visit[state][yy][xx]=index+1
#                                 temp_q.append((yy,xx,state))                                 
#             if temp_q:
#                 q = temp_q
#                 time= not time
#         print(-1)
#     bfs()


            














