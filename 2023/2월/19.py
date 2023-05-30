import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15685
# from collections import deque
# n_list = [[0]*101 for _ in range(101)]
# visited = [[False]*101 for _ in range(101)]
# move = [(0,1),(-1,0),(0,-1),(1,0)]
# for _ in range(one()):
#     x,y,d,g = wow()
#     visited[y][x]=True
#     q = []
#     move_y,move_x = move[d]
#     q.append(d)
#     visited[y+move_y][x+move_x]=True
#     x+=move_x
#     y+=move_y
#     # print(q)
#     for _ in range(g):
#         temp_list = []
#         for i in q[::-1]:
#             index = (i+1)%4
#             temp_list.append(index)
#             move_y,move_x = move[index]
#             visited[y+move_y][x+move_x]=True
#             x+=move_x
#             y+=move_y
#         # print(q,temp_list)
#         q = q+temp_list
#     # print("end",q)
# def check(y,x):
#     cnt = 0
#     if visited[y+1][x]:
#         cnt+=1
#     if visited[y+1][x+1]:
#         cnt+=1
#     if visited[y][x+1]:
#         cnt+=1
#     if cnt == 3:
#         return True
#     else:
#         return False 
# count = 0
# for y in range(101-1):    
#     for x in range(101-1):    
#         if visited[y][x]== True:
#             if check(y,x):
#                 count+=1
# print(count)













