import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# from collections import deque
# n,gap_min,gap_max = wow()
# n_list=[list(wow()) for i in range(n)]
# time = 0
# q = deque()
# q.append((0,0))
# move= [(1,0),(0,1),(-1,0),(0.-1)]
# while q:
#     temp=deque()
#     visited = [[False]*n for i in range(n)]
#     y,x=q.popleft()
#     standard = n_list[y][x]
#     visited[y][x]=True
#     for a,b in move:
#         yy,xx = y+a,x+b
#         if 0<=yy<=n-1 and 0<=xx<=n-1:
#             s = n_list[yy][xx]
#             if gap_min<=abs(s-standard)<=gap_max:
#                 temp.append((yy,xx))

#https://www.acmicpc.net/problem/27433
# n = one()
# cnt = 1
# for i in range(2,n+1):
#     cnt*=i
# print(cnt)













