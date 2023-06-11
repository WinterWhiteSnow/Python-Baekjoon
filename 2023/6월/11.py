import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/18290
# r,c,k = wow()
# n_list = [list(wow()) for _ in range(r)]
# max_max ="none"
# visit = [[0]*c for _ in range(r)]
# def check(y,x,v):
#     global r,c
#     move = [(1,0),(0,1),(0,-1),(-1,0)]
#     new_list = []
#     for my,mx in move:
#         yy,xx=my+y,mx+x
#         # print("yy,xx",yy,xx)
#         if 0<=yy<r and 0<=xx<c:
#             if v[yy][xx]==0:
#                 new_list.append((yy,xx))
#     return new_list
# def go(v,total,cnt,yy,xx):
#     global r,c,k,max_max
#     if cnt < k:
#         for y in range(yy,r):
#             for x in range(xx if y==yy else 0,c):
#                 if v[y][x]==0:
#                     v[y][x]=1
#                     list_list = check(y,x,v)
#                     for y_index,x_index in list_list:
#                         v[y_index][x_index]=1
#                     go(v,total+n_list[y][x],cnt+1,y,x)
#                     v[y][x]=0
#                     for y_index,x_index in list_list:
#                         v[y_index][x_index]=0
#     else:
#         if max_max == "none":
#             max_max = total
#         else:
#             max_max=max(max_max,total)
# go(visit,0,0,0,0)
# print(max_max)     
           














