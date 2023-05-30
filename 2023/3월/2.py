import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17070
# y,x = 0,1
# n = one()
# visit = [list(wow()) for _ in range(n)]   
# move = [(0,1),(1,0),(1,1)]
# move_index = 0
# check = [[(0,1)],[(1,0)],[(0,1),(1,0),(1,1)]]
# count = 0
# d = 0
# def go(y,x,index):
#     global n,count
#     # print("Start",y,x,index)
#     if y==n-1 and x==n-1:
#         count+=1
#         return
#     if index == 0:
#         if x+1 < n:
#             if visit[y][x+1]==False:
#                 go(y,x+1,0)
#                 if y+1<n:
#                     if visit[y+1][x] == visit[y+1][x+1]==False:
#                         go(y+1,x+1,2)
#     elif index == 1:
#         if y+1 < n:
#             if visit[y+1][x]==False:
#                 go(y+1,x,1)
#                 if x+1<n:
#                     if visit[y][x+1] == visit[y+1][x+1]==False:
#                         go(y+1,x+1,2)
#     else:
#         if x+1 < n:
#             if visit[y][x+1]==False:
#                 go(y,x+1,0)
#                 if y+1<n:
#                     if visit[y+1][x] == visit[y+1][x+1]==False:
#                         go(y+1,x+1,2)
#         if y+1<n:
#             if visit[y+1][x] == False:
#                 go(y+1,x,1)
# go(y,x,move_index)
# print(count)

















