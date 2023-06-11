import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://school.programmers.co.kr/learn/courses/30/lessons/43105
# def solution(triangle):
#     n_list = triangle
#     l = len(triangle)
#     for down in range(1,l):
#         for index in range(len(n_list[down])):
#             if index == 0:
#                 n_list[down][0]+=n_list[down-1][0]
#             elif index ==  len(n_list[down])-1:
#                 n_list[down][-1]+=n_list[down-1][-1]
#             else:
#                 n_list[down][index]+=max(n_list[down-1][index-1],n_list[down-1][index])
#     return max(n_list[-1])

#https://www.acmicpc.net/problem/14940
# from collections import deque
# r,c = wow()
# n_list = [list(wow()) for _ in range(r)]
# visit = [[0]*c for _ in range(r)]
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# start_y,start_x = "none","none"
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == 2:
#             start_y,start_x=y,x
#             break
#     if start_y != "none":
#         break
# q = deque()
# q.append((start_y,start_x))
# visit[start_y][start_x]=0
# n_list[start_y][start_x]=0
# while len(q)>0:
#     y,x = q.popleft()
#     num = n_list[y][x]
#     for my,mx in move:
#         yy,xx = my+y,mx+x
#         if 0<=yy<r and 0<=xx<c:
#             if visit[yy][xx]==0:
#                 visit[yy][xx]=1
#                 if n_list[yy][xx] == 1:
#                     n_list[yy][xx]=num+1
#                     q.append((yy,xx))
# for y in range(r):
#     for x in range(c):
#         if visit[y][x] == 0 and n_list[y][x]==1:
#             n_list[y][x]=-1
# for i in n_list:
#     print(*i)

#https://school.programmers.co.kr/learn/courses/30/lessons/42626#
# import heapq
# cnt = 0
# def solution(scoville, K):
#     global cnt
#     k=K
#     answer = 0
#     h = []
#     for i in scoville:
#         heapq.heappush(h,i)
#     if len(h)>=2:
#         while len(h)>=2:
#             a = heapq.heappop(h)
#             if a >=k:
#                 return cnt
#             else:
#                 cnt+=1
#                 b = heapq.heappop(h)
#                 heapq.heappush(h,a+b*2)
#         if h.pop()>=k:
#             return cnt
#         else:
#             return -1
#     else:
#         if len(h)>0:
#             a= h.pop()
#             if a>=k:
#                 return 0
#             else:
#                 return -1
#         else:
#             return -1
                
            

        
    return -1
            
    
            













