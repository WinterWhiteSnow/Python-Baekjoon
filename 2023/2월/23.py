import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17142
# from collections import deque
# n,k = wow()
# n_list = [list(wow()) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]
# index_list = []
# total = 0
# zero_visit = [[False]*n for _ in range(n)]
# for y in range(n):
#     for x in range(n):
#         if n_list[y][x] != 0:
#             if n_list[y][x] == 2:
#                 index_list.append((y,x))
#                 n_list[y][x] = "*"
#             if n_list[y][x] == 1:
#                 visited[y][x]=True
#                 n_list[y][x]="X"
#         else:
#             zero_visit[y][x]=True
#             total+=1
# move = [(-1,0),(1,0),(0,1),(0,-1)]
# cnt = 10000000000000000000000000000001
# l = len(index_list)
# def check(visit):
#     global n
#     for y in range(n):
#         for x in range(n):
#             if visit[y][x]==False:
#                 return False
#     return True
# def go(count,visited,index_index,index_list,now_list):
#     global k,l,n,cnt,total,zero_visit
#     if count < k:
#         if index_index+1 < l:
#             for i in range(index_index+1,l):
#                 now_list.append(i)
#                 count+=1
#                 go(count,visited,i,index_list,now_list)
#                 count-=1
#                 now_list.pop()
#     else:
#         cnt_cnt_cnt = total
#         q=deque()
#         for i in now_list:
#             q.append(index_list[i])
#         time = 0
#         visit = []
#         for v in zero_visit:
#             a = []
#             for vv in v:
#                 a.append(vv)
#             visit.append(a)
#         front = [] #벽
#         for b in visited:
#             bb = []
#             for bbb in b:
#                 bb.append(bbb)
#             front.append(bb)
#         while True:
#             temp_list = deque()
#             while q:
#                 y,x = q.popleft()
#                 front[y][x]=True
#                 for yy,xx in move:
#                     yyy,xxx = y+yy,xx+x
#                     if 0<=yyy<n and 0<=xxx<n:
#                         if front[yyy][xxx]== False:
#                             front[yyy][xxx]=True
#                             if visit[yyy][xxx]==True:
#                                 visit[yyy][xxx]=False
#                                 cnt_cnt_cnt-=1
#                             temp_list.append((yyy,xxx))               
#             # print("now!!!",time,cnt_cnt_cnt,temp_list)
#             # for i in range(n):
#             #     print(*visit[i])
#             if temp_list:
#                 if cnt_cnt_cnt <= 0:
#                     time+=1
#                     break 
#                 else:         
#                     time+=1
#                     q = temp_list
#             else:
#                 break
#         if cnt_cnt_cnt == 0:
#             if cnt> time:
#                 cnt = time
# b = "yes"
# for y in range(n):        
#     for x in range(n):
#         if n_list[y][x] == 0:
#             b = "no"
#             break
#     if b == "no":
#         break
# if b == "no":
#     for i in range(l):
#         go(1,visited,i,index_list,[i])    
#     print(cnt if cnt != 10000000000000000000000000000001 else -1)            
# else:
#     print(0)














