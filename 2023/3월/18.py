import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9328
# import string
# str_str = list(string.ascii_lowercase)
# STR_STR = list(string.ascii_uppercase)
# key_dict = {}
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# for a in range(26):
#     key_dict[str_str[a]]=a
# def bfs(enter_list,visit):
#     global r,c,cnt
#     q = deque()
#     q.extend(enter_list)
#     before = False
#     while q:
#         v = [] 
#         for a in visit:
#             f = []
#             for aa in a:
#                 f.append(aa)
#             v.append(f)
#         temp_list = deque()
#         while q:
#             y,x = q.popleft()
#             v[y][x]=True
#             if n_list[y][x].isupper():
#                 if key[STR_STR.index(n_list[y][x])] == False:
#                     continue
#             if n_list[y][x]=="$":
#                 if document[y][x]:
#                     document[y][x]=0
#                     cnt+=1
#             for yy,xx in move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if v[yyy][xxx]==False:
#                         if n_list[yyy][xxx] ==".":
#                             q.append((yyy,xxx))
#                             v[yyy][xxx]=True
#                             temp_list.append((yyy,xxx))
#                         elif n_list[yyy][xxx] == "$":
#                             if document[yyy][xxx]:
#                                 document[yyy][xxx]=0
#                                 cnt+=1
#                                 # q.append((yyy,xxx))
#                             q.append((yyy,xxx))
#                             v[yyy][xxx]=True
#                             temp_list.append((yyy,xxx))
#                         else:
#                             if n_list[yyy][xxx].islower():
#                                 key[key_dict[n_list[yyy][xxx]]]=True
#                                 q.append((yyy,xxx))
#                                 v[yyy][xxx]=True
#                                 temp_list.append((yyy,xxx))
#                             else:
#                                 if n_list[yyy][xxx].isupper():
#                                     index = STR_STR.index(n_list[yyy][xxx])
#                                     if key[index]:
#                                         q.append((yyy,xxx))
#                                         v[yyy][xxx]=True
#                                         temp_list.append((yyy,xxx))
#         if before != temp_list:
#             before = temp_list
#             q.extend(enter_list)
#     print(cnt)
# for _ in range(one()):
#     r,c = wow()
#     n_list = [list(inputing()) for _ in range(r)]
#     enter_list = deque()
#     visit = [[False]*c for _ in range(r)]
#     cnt = 0
#     document = [[False]*c for _ in range(r)]
#     key = [0]*26
#     for y in range(r):
#         for x in range(c):
#             if n_list[y][x]=="*":
#                 visit[y][x]=True
#             elif n_list[y][x] == "$":
#                 document[y][x]=True
#             if y==0 or y==r-1:
#                 if n_list[y][x]==".":
#                     enter_list.append((y,x))
#                 if n_list[y][x].islower():
#                     enter_list.append((y,x))
#                     key[str_str.index(n_list[y][x])]=1
#                 if n_list[y][x].isupper():
#                     enter_list.append((y,x))
#                 if n_list[y][x]=="$":
#                     enter_list.append((y,x))
#             if x==0 or x==c-1:
#                 if y==x==0:
#                     continue
#                 if x==0 and y == r-1:
#                     continue
#                 if x == c-1 and y == 0:
#                     continue
#                 if x == c-1 and y == r-1:
#                     continue
#                 if n_list[y][x]==".":
#                     enter_list.append((y,x))
#                 if n_list[y][x].islower():
#                     enter_list.append((y,x))
#                     key[str_str.index(n_list[y][x])]=1
#                 if n_list[y][x].isupper():
#                     enter_list.append((y,x))
#                 if n_list[y][x]=="$":
#                     enter_list.append((y,x))
#     key_list = list(inputing())
#     if key_list[0] == "0":
#         pass
#     else:
#         for i in key_list:
#             key[key_dict[i]]=1
#     bfs(enter_list,visit)

#https://www.acmicpc.net/problem/3055
# r,c = wow()
# n_list = [list(inputing()) for _ in range(r)]
# visit = [[False]*c for _ in range(r)]  
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# water = deque()
# q = deque()       
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == "*":
#             water.append((y,x))
#             visit[y][x]=True
#         if n_list[y][x] == "X":
#             visit[y][x]=True
#         if n_list[y][x] == "S":
#             start_y,start_x = y,x
#             q.append((y,x))
#         if n_list[y][x]=="D":
#             end_y,end_x = y,x
# time = 0
# while q:
#     time+=1
#     temp_list = deque()
#     temp_water = deque()
#     while water:
#         y,x = water.popleft()
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if visit[yyy][xxx]==False and n_list[yyy][xxx] != "D":
#                     visit[yyy][xxx]=True
#                     temp_water.append((yyy,xxx))
#                 if visit[yyy][xxx]=="X" and n_list[yyy][xxx] != "D":
#                     visit[yyy][xxx]=True
#                     temp_water.append((yyy,xxx))
#     while q:
#         y,x = q.popleft()
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if yyy==end_y and xxx==end_x:
#                 print(time)
#                 exit()
#             if 0<=yyy<r and 0<=xxx<c:
#                 if visit[yyy][xxx]==False:
#                     visit[yyy][xxx]="X"
#                     temp_list.append((yyy,xxx))
#     # print(temp_water)
#     # print(temp_list)
#     # print(time)
#     # for i in visit:
#     #     print(i)
#     if temp_water:
#         water = temp_water
#     if temp_list:
#         q = temp_list
#     # exit()    
# print("KAKTUS")  

   
        
            
        
        














