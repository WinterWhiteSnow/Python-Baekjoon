import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/7576
# l,r = wow()
# n_list = [list(wow()) for _ in range(r)]
# index_list = []
# zero_cnt = 0
# for y in range(r):
#     for x in range(l):
#         if n_list[y][x] == 1:
#             index_list.append([y+1,x])
#             index_list.append([y-1,x])
#             index_list.append([y,x-1])
#             index_list.append([y,x+1])
#         elif n_list[y][x]==0:
#             zero_cnt+=1
# cnt = 0
# visited= [[False]*l for _ in range(r)]
# while index_list:
#     # print("start",index_list,cnt)
#     temp_list = []
#     while index_list:
#         y,x = index_list.pop()
#         if 0<=y<=r-1 and 0<=x<=l-1:
#             if visited[y][x] == False:
#                 visited[y][x] = True
#                 if n_list[y][x] == 0:
#                     n_list[y][x]=1
#                     zero_cnt-=1
#                     temp_list.append([y-1,x])
#                     temp_list.append([y+1,x])
#                     temp_list.append([y,x-1])
#                     temp_list.append([y,x+1])
#     cnt+=1
#     # print(cnt)
#     # for i in n_list:
#     #     print(*i)
#     index_list=temp_list
# print(-1 if zero_cnt != 0 else cnt-1)

def dfs(y,x,visited):
    visit = []
    for i in visited:
        v = []
        for ii in i:
            v.append(ii)
        visit.append(v)
    if visit[y][x]==False:
        visit[y][x]=True
        
    
    
for _ in range(one()):
    l = one()
    n_list = [list(wow()) for _ in range(2)]
    visited = [[False]*l for _ in range(2)]
    dfs(0,0,visited)
    dfs(0,1,visited)
















