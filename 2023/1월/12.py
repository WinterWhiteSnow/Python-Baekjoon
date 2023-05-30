import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/4108
# def go(y,x,list_list,r,l):
#     if 0<=y<=r-1 and 0<=x<=l-1:
#         if list_list[y][x]=="*":
#             return 1
#     return 0
# while True:
#     r,l = wow()
#     if r==l==0:
#         break
#     n_list = [list(inputing()) for _ in range(r)]
#     for y in range(r):
#         for x in range(l):
#             if n_list[y][x]==".":
#                 cnt = 0
#                 for y_index in range(y-1,y+2):
#                     for x_index in range(x-1,x+2):
#                         cnt+=go(y_index,x_index,n_list,r,l)
#                 n_list[y][x]=cnt
#     for i in n_list:
#         print(*i,sep="")                














