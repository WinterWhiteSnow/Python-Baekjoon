import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17086
# from collections import deque
# r,c = wow()
# q = deque()
# move = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
# n_list = [list(wow()) for _ in range(r)]
# max_max = 0
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == False:
#             gap = 10000000000000001
#             visit = [[False]*c for _ in range(r)]
#             q = deque()
#             q.append((y,x,0))
#             visit[y][x]=True
#             while q:
#                 yy,xx,cnt = q.popleft()
#                 for yyy,xxx in move:
#                     yyyy,xxxx = yy+yyy,xx+xxx
#                     if 0<=yyyy<r and 0<=xxxx<c:
#                         if visit[yyyy][xxxx]==False:
#                             visit[yyyy][xxxx]=True
#                             if n_list[yyyy][xxxx]:
#                                 gap = min(gap,cnt+1)
#                             else:
#                                 q.append((yyyy,xxxx,cnt+1))
#             max_max=max(gap,max_max)          
# print(max_max)        

#https://www.acmicpc.net/problem/16967
# r,c,x,y = wow()
# n_list = [list(wow()) for _ in range(r+x)]
# answer = []
# for yy in range(r):
#     list_list = []
#     for xx in range(c):
#         if x<=yy and y<=xx:
#             list_list.append(n_list[yy][xx]-n_list[yy-x][xx-y])
#             n_list[yy][xx] = n_list[yy][xx]-n_list[yy-x][xx-y]
#         else:
#             # print(yy,xx)
#             list_list.append(n_list[yy][xx])
#     answer.append(list_list)
# for i in answer:
#     print(*i)

#https://www.acmicpc.net/problem/16918
# from collections import deque
# time = 0
# r,c,after = wow()
# n_list = [list(inputing()) for _ in range(r)]
# cnt = 0
# index_list= deque()
# move = [(0,1),(1,0),(0,-1),(-1,0)]
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == "O":
#             index_list.append((y,x))
# def bomb(list_list):
#     global r,c
#     temp_list = deque()
#     for y,x in list_list:
#         n_list[y][x] = "."
#         for yy,xx in move:
#             yyy,xxx = y+yy,x+xx
#             if 0<=yyy<r and 0<=xxx<c:
#                 n_list[yyy][xxx]="."
#     for y in range(r):
#         for x in range(c):
#             if n_list[y][x] == "O":
#                 temp_list.append((y,x))
#     return temp_list

# while cnt<after:
#     if time == cnt == 0:
#         pass
#     else:
#         if time==1:
#             for y in range(r):
#                 for x in range(c):
#                     if n_list[y][x]==".":
#                         n_list[y][x]="O"
#         else:
#             index_list = bomb(index_list)
#     time+=1
#     time%=2
#     cnt+=1
# for i in n_list:
#     print(*i,sep="")

#https://www.acmicpc.net/problem/13335
# from collections import deque
# l,m,limit = wow()
# n_list = deque(list(wow()))
# time = 0
# q = deque([0]*m)
# while n_list:
#     time+=1
#     q.popleft()
#     # print(n_list[0],sum(q))
#     if n_list[0]+sum(q)<=limit:
#         q.append(n_list.popleft())
#     else:
#         q.append(0)
#     # print(time,q)
# print(time+len(q))

#https://www.acmicpc.net/problem/18428
# from collections import deque
# r = one()
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# n_list = [inputing().split() for _ in range(r)]
# t_list = deque()
# visit = [[False]*r for _ in range(r)]
# for y in range(r):
#     for x in range(r):
#         if n_list[y][x] == "T":
#             t_list.append((y,x))
#             visit[y][x]="T"
#         if n_list[y][x] == "S":
#             visit[y][x]="S"
# check = False
# def dfs(list_list,cnt,v,t_list):
#     global check,r
#     if cnt <3:
#         for y in range(r):
#             for x in range(r):
#                 if n_list[y][x] == "X":
#                     if v[y][x] == False:
#                         list_list.append((y,x))
#                         v[y][x]="W"
#                         dfs(list_list,cnt+1,v,t_list)
#                         v[y][x]=False
#                         list_list.pop()
#     else:
#         check_list = []
#         # for i in v:
#         #     print(i)
#         for y,x in t_list:
#             state = True
#             for yy,xx in move:
#                 start_y,start_x = y,x
#                 while 0<=start_y+yy<r and 0<=start_x+xx<r:
#                     if v[start_y+yy][start_x+xx] == False:
#                         start_y+=yy
#                         start_x+=xx
#                     else:
#                         if v[start_y+yy][start_x+xx]=="W":
#                             break
#                         elif v[start_y+yy][start_x+xx]=="S":
#                             state = False
#                             break
#                         else:
#                             start_y+=yy
#                             start_x+=xx
#                 if state == False:
#                     break
#             check_list.append(state)
#         if set(check_list) == {True}:
#             check = True              
# dfs(deque(),0,visit,t_list)            
# print("YES" if check else "NO")
    



            
                    
    
    



    












