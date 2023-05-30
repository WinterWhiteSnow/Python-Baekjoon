import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())
#https://www.acmicpc.net/problem/16927

# import math
# from collections import deque
# def go(y,x):
#     # print("Start!",y,x)
#     list_list = deque()
#     start_y,start_x=y,x
#     global r,c
#     index= 0
#     state = False
#     while True:
#         my,mx = move[index]
#         if y==start_y and x==start_x:
#             if state:
#                 return list_list
#         while 0<=my+y<r and 0<=mx+x<c:
#             # print("현재위치",y,x,"이동방향",index)
#             # print("다음위치",my+y,mx+x)
#             if visit[my+y][mx+x]==0:
#                 visit[my+y][mx+x]=1
#                 list_list.append((y,x))            
#                 y,x = my+y,mx+x
#             else:
#                 break
#             state = True
#         index+=1
#         index%=4
# r,c,k = wow()
# sero,garo = r,c
# n_list = [list(wow()) for _ in range(r)]
# visit = [[0]*c for _ in range(r)]
# new_list = [[0]*c for _ in range(r)]
# for repeat in range(min(r,c)//2):
#     move = [(1,0),(0,1),(-1,0),(0,-1)]
#     paint= False
#     for y in range(r):
#         for x in range(c):
#             if visit[y][x]==0:
#                 a = go(y,x)
#                 paint = True
#                 break
#         if paint:
#             break
#     b = [i for i in a]
#     if repeat == 0:
#         pass
#     else:
#         sero-=2
#         garo-=2
#     rotate = (sero-1)*2+(garo-1)*2
#     rotate = k%rotate
#     a.rotate(-rotate)
#     for i in range(len(a)):
#         y,x = a[i]
#         num_y,num_x =b[i]
#         num = n_list[num_y][num_x]
#         new_list[y][x]=num 
# for i in new_list:
#     print(*i)














