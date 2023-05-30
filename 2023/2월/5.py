import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# #https://www.acmicpc.net/problem/2436
# from collections import deque
# from math import gcd
# n = list(wow())
# a,b = sorted(n)
# if a==b:
#     print(a,b)
# elif b%a != 0:
#     print(1,1)
# else:
#     n_list = []
#     key=set()
#     key.add(a)
#     key.add(b)
#     ndict={}
#     index = 0

#     xx,yy = 1000000000000001,1000000000000001
#     for i in range(1,int((a*b)**(1/2))+1):
#         if b%i == 0:
#             key.add(i)
#             key.add(b//i)
#     key = sorted([i for i in key if i%a == 0])
#     for i in range(len(key)-1):
#         for ii in range(i+1,len(key)):
#             # print(i,ii)
#             x,y = key[i],key[ii]
#             if x*y//gcd(x,y) == b:
#                 if x%a == y%a == 0:
#                     if abs(xx+yy) > abs(x+y):
#                         xx,yy=x,y
#     print(min(xx,yy),max(xx,yy))
#     # print(key.index(11648),key.index(14850))
#     # print(gcd(11648,14850),11648*14850//gcd(11648,14850))

#https://www.acmicpc.net/problem/14502
# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# visited = [[False]*l for _ in range(r)]
# for y in range(r):
#     for x in range(l):
#         if n_list[y][x] != 0:
#             visited[y][x] = True
# count = 0        
# def check(n_list):
#     # for i in n_list:
#     #     print(*i)
#     b_list = []
#     for i in n_list:
#         b = []
#         for a in i:
#             b.append(a)
#         b_list.append(b)

#     global r
#     global l
#     global count
#     index_list = []
#     visit = [[False]*l for _ in range(r)]
#     for y in range(r):
#         for x in range(l):
#             if b_list[y][x] == 2:
#                 visit[y][x]=True
#                 index_list.append((y,x))
#             elif b_list[y][x]==1:
#                 visit[y][x]=True
#     move = [(1,0),(-1,0),(0,1),(0,-1)]
#     # print(index_list)
#     # print("visited")
#     # for i in visit:
#     #     print(*i)
#     # exit()
#     while index_list:
#         y,x = index_list.pop()
#         for a,b in move:
#             yy,xx = y+a,x+b
#             # print(yy,xx)
#             if 0<= yy<= r-1 and 0<=xx<=l-1:
#                 # print("범위 들어옴01",visit[yy][xx]==False,b_list[yy][xx]==0)
#                 if visit[yy][xx] == False and b_list[yy][xx]==0:
#                     # print("correct!!!",yy,xx)
#                     visit[yy][xx]= True
#                     b_list[yy][xx]=2
#                     index_list.append((yy,xx))
#         # print(index_list)
#     # print("end!!!")
#     # for i in b_list:
#     #     print(*i)
#     cnt = 0
#     for y in range(r):
#         # print(*b_list[y])
#         for x in range(l):
#             if b_list[y][x] == 0:
#                 cnt+=1
#     if cnt > count:
#         count = cnt
    
        
# def go(visited,count):
#     # print("start!!",count)
#     global r
#     global l
#     if count == 3:
#         # print(333333)
#         # for i in n_list:
#         #     print(*i)
#         check(n_list)
#         return
#     if count < 3:
#         for y in range(r):
#             for x in range(l):
#                 if n_list[y][x] == 0:
#                     n_list[y][x]=1
#                     visited[y][x]=True
#                     count+=1
#                     go(visited,count)
#                     n_list[y][x]=0
#                     visited[y][x]=False
#                     count-=1
# go(visited,0)
# print(count)


    






