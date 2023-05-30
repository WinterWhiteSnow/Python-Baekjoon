import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17136
# index = 5
# n_list = [list(wow()) for _ in range(10)]
# cnt = 0
# total = [5]*6
# visit = [[False]*10 for _ in range(10)]
# count = 0
# for y in range(10):
#     for x in range(10):
#         count+=n_list[y][x]
# def check(y,x,index,list_list):
#     for yy in range(y,y+index):
#         for xx in range(x,x+index):
#             if list_list[yy][xx] == 0:
#                 return False
#     return True
# min_min = 100000000000000000000000000001
# def go(list_list,total,index,cnt,count):
#     global min_min
#     if min_min <= cnt:
#         return
#     b = 0
#     for i in range(1,index+1):
#         b+=total[i]*(i**2)
#     if b < count:
#         return
#     if index>1 and total[index]>0:
#         for y in range(10-index+1):            
#             for x in range(10-index+1):            
#                 if list_list[y][x] == 1 and total[index]>0 and check(y,x,index,list_list):
#                     for yy in range(y,y+index):
#                         for xx in range(x,x+index):
#                             list_list[yy][xx]=0
#                     total[index]-=1
#                     go(list_list,total,index,cnt+1,count-index*index)
#                     for yy in range(y,y+index):
#                         for xx in range(x,x+index):
#                             list_list[yy][xx]=1
#                     total[index]+=1
#         go(list_list,total,index-1,cnt,count)
#     else:
#         if count > 5:
#             return    
#         if min_min>cnt+count:
#             min_min = cnt+count
# go(n_list,total,5,0,count)       
# print(-1 if min_min == 100000000000000000000000000001 else min_min)

r = one()
n_list = [list(wow()) for _ in range(r)]













