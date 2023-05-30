import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9205
# def bfs(start_x,start_y,visited,list_list,l):
#     global g_x,g_y
#     q = [[start_x,start_y]]
#     while q:
#         # print(q,visited)
#         x,y = q.pop()
#         if abs(x-g_x)+abs(y-g_y)<=1000:
#             print("happy")
#             return
#         for i in range(l):
#             if not visited[i]:
#                 go_x,go_y = list_list[i]
#                 # print("go!",go_x,go_y)
#                 if abs(go_x-x)+abs(go_y-y) <= 1000:
#                     q.append([go_x,go_y]) 
#                     visited[i]=not visited[i]
#     print("sad")   
# for _ in range(one()):
#     r = one()
#     x,y = wow()
#     n_list = [list(wow()) for _ in range(r)]
#     g_x,g_y = wow()
#     n_list.sort(key=lambda x: (abs(x[0])+abs(x[1])))
#     visited = [False]*r
#     check_list = []
#     bfs(x,y,visited,n_list,r)

#https://www.acmicpc.net/problem/2573
# sys.setrecursionlimit(10**6)
# from collections import deque
# r,l= wow()
# n_list = deque(deque(wow()) for _ in range(r))
# cnt = 0
# index_list = deque()
# zero_cnt = 0
# for y in range(r):
#     for x in range(l):
#         if n_list[y][x] != 0:
#             index_list.append([y,x])
#         else:
#             zero_cnt+=1
# def go(y,x,r,l,n_list):
#     if 0<=y<=r-1 and 0<=x<=l-1:
#         if n_list[y][x] == 0:
#             return 1
#     return 0

# def bfs(y,x,visited,list_list):
#     q = [[y,x]]
#     while q:
#         y,x = q.pop()
#         if x<=-1 or x>=l or y<=-1 or y>=r:
#             continue
#         if visited[y][x] ==False:
#             visited[y][x]=True
#             if list_list[y][x] != 0:
#                 q.append([y-1,x])
#                 q.append([y+1,x])
#                 q.append([y,x-1])
#                 q.append([y,x+1])
# count = 0
# visited = [[False]*l for _ in range(r)]
# for i in index_list:
#     y,x = i
#     if visited[y][x] ==False:
#         bfs(y,x,visited,n_list)
#         count+=1
# if count > 1:
#     print(cnt)
# else:                     
#     if zero_cnt != 0:               
#         while index_list:
#             temp_list = deque()
#             list_list = deque(deque([0]*l) for _ in range(r))
#             while index_list:
#                 y,x = index_list.popleft()
#                 count = 0
#                 count+=go(y-1,x,r,l,n_list)
#                 count+=go(y,x+1,r,l,n_list)
#                 count+=go(y+1,x,r,l,n_list)
#                 count+=go(y,x-1,r,l,n_list)
#                 index = max(0,n_list[y][x]-count)
#                 if index > 0:
#                     temp_list.append([y,x])
#                 list_list[y][x]=index
#             cnt+=1
#             count = 0
#             visited = [[False]*l for _ in range(r)]
#             for i in temp_list:
#                 y,x = i
#                 if visited[y][x] == False:
#                     bfs(y,x,visited,list_list)
#                     count+=1
#             if count > 1:
#                 print(cnt)
#                 exit()
#             index_list=temp_list
#             n_list = list_list
#         print(0)
#     else:
#         print(0)

            
l,r = wow()
n_list = [list(wow()) for _ in range(l)]



















