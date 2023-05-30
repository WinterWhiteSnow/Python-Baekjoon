import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15723
# import string
# str_str = list(string.ascii_lowercase)
# n_dict = {}
# for a,b in enumerate(str_str):
#     n_dict[b]=a
# visit = [[0]*26 for _ in range(26)]
# for _ in range(one()):
#     x,y = inputing().split("is")
#     x,y = x.replace(" ",""), y.replace(" ","")
#     xx,yy = n_dict[x],n_dict[y]
#     visit[xx][yy]=1
# for _ in range(one()):
#     x,y = inputing().split("is")
#     x,y = x.replace(" ",""), y.replace(" ","")
#     xx,yy = n_dict[x],n_dict[y]
#     state = False
#     if visit[xx][yy]== 1:
#         state= True
#     else:
#         q = deque()
#         q.append(xx)
#         while q:
#             f = q.popleft()
#             # print("start!",f,visit[f])
#             for k in range(26):
#                 if visit[f][k]==1:
#                     # print(f,"????",k)
#                     if k == yy:
#                         state = True
#                         break
#                     else:
#                         q.append(k)                   
#             if state == True:
#                 break
#     print("T" if state else "F")

#https://www.acmicpc.net/problem/3184
# r,c = wow()
# n_list = [list(inputing()) for _ in range(r)]        
# visit = [[False]*c for _ in range(r)]
# move = [(1,0),(0,1),(0,-1),(-1,0)]

# def bfs(y,x):
#     global r,c
#     q = deque()
#     q.append((y,x))
#     sheep = 0
#     wolf = 0
#     visit[y][x]=True
#     # print("Start!",y,x,n_list[y][x])
#     if n_list[y][x] == "v":
#         wolf+=1
#     if n_list[y][x] == "o":
#         sheep+=1
#     if n_list[y][x] == "#":
#         return [0,0]
#     while q:
#         y,x = q.popleft()
#         # print(y,x,q,sheep,wolf)
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 # print(y,x,yyy,xxx,visit[yyy][xxx])
#                 if visit[yyy][xxx]==False:
#                     visit[yyy][xxx] = True
#                     if n_list[yyy][xxx] == "#":
#                         continue
#                     if n_list[yyy][xxx] == "o":
#                         sheep+=1
#                         q.append((yyy,xxx))
#                     if n_list[yyy][xxx] == "v":
#                         wolf+=1
#                         q.append((yyy,xxx))
#                     if n_list[yyy][xxx] == ".":
#                         q.append((yyy,xxx))
#     # print(sheep,wolf)
#     if sheep > wolf:
#         return [sheep,0]
#     else:
#         return [0,wolf]
# s= 0
# w = 0                    
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == "#":
#             visit[y][x]=True
# for y in range(r):
#     for x in range(c):
#         if visit[y][x] == False:
#             visit[y][x]=True
#             a,b = bfs(y,x)
#             s+=a
#             w+=b
#             # print(y,x,s,w)
#             # for i in visit:
#             #     print(i)
# # bfs(1,5)
# print(s,w)

#https://www.acmicpc.net/problem/3048
# a,b = wow()
# a_list = [1]*a
# b_list = [-1]*b
# visit = a_list+b_list
# l = a+b
# list_list = list(inputing()[::-1]+inputing())
# t = one()
# time = 0
# for _ in range(t):
#     index = 0
#     while index+1 <a+b:
#         x,y = visit[index],visit[index+1]
#         if x==1 and y==-1:
#             visit[index],visit[index+1]=visit[index+1],visit[index]
#             list_list[index],list_list[index+1]=list_list[index+1],list_list[index]
#             index+=2
#         else:
#             index+=1
# print("".join(list_list))            

#https://www.acmicpc.net/problem/2784
# n_list = [inputing() for _ in range(6)]
# n_list.sort()
# for x in range(6):
#     for y in range(6):
#         for z in range(6):
#             if x==y or y==z or x==z:
#                 continue
#             list_list = [n_list[x],n_list[y],n_list[z]]
#             n_dict = {}
#             visit = [0]*6 
#             for n in [x,y,z]:
#                 visit[n]=1
#             for i in range(3):
#                 n_dict[i]=""
#                 for j in range(3):
#                     n_dict[i]+=list_list[j][i]
#             check = sorted(n_dict.values())
#             str_list = []
#             for index in range(6):
#                 if visit[index] == 0:
#                     str_list.append(n_list[index])
#             # print(check,str_list)
#             if check == str_list:
#                 print(*list_list,sep="\n")
#                 exit()
# print(0)
          
          
#https://www.acmicpc.net/problem/2589
# r,c = wow()
# n_list = [inputing() for _ in range(r)]
# move = [(0,1),(1,0),(-1,0),(0,-1)]
# max_max = 0
# def dfs(y,x):
#     q = deque()
#     q.append((y,x,0))
#     visit = [[0]*c for _ in range(r)]
#     visit[y][x] = True
#     count = 0
#     while q:
#         y,x,cnt = q.popleft()
#         if cnt > count:
#             count = cnt
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if visit[yyy][xxx] == False:
#                     visit[yyy][xxx] = True
#                     if n_list[yyy][xxx] == "L":
#                         q.append((yyy,xxx,cnt+1))
#     return count    
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == "L":
#             num = dfs(y,x)
#             if max_max < num:
#                 max_max = num
# print(max_max)

#https://www.acmicpc.net/problem/2638
# r,c = wow()
# n_list = [list(wow()) for _ in range(r)]
# move = [(0,1),(1,0),(-1,0),(0,-1)]
# def check(y,x):
#     global r,c
#     cnt = 0
#     for yy,xx in move:
#         yyy,xxx = yy+y,xx+x
#         if 0<=yyy<r and 0<=xxx<c:
#             if visit[yyy][xxx] == -1:
#                 cnt+=1
#     if cnt >= 2:
#         return True
#     return False
# time = 0
# while True:
#     index_list = []
#     visit = [[0]*c for _ in range(r)]
#     q = deque()
#     q.append((0,0))
#     visit[0][0]=-1
#     while q:
#         y,x = q.popleft()
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if n_list[yyy][xxx] == 0 and visit[yyy][xxx] == 0:
#                     visit[yyy][xxx]=-1
#                     q.append((yyy,xxx))
#     for y in range(r):
#         for x in range(c):
#             if n_list[y][x] == 1:
#                 if check(y,x):
#                     index_list.append((y,x))
#     if len(index_list)>0:
#         time+=1
#         for y,x in index_list:
#             n_list[y][x]=0
#     else:
#         break
#     # print("now")
#     # for i in n_list:
#     #     print(i)
# print(time)


    










