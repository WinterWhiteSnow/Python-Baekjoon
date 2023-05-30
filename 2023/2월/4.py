import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15684
# n,r,lines = wow()
# if r == 0:
#     print(0)
# else:
#     def check(visited):
#         global n
#         global lines
#         check = "yes"
#         for state in range(1,n+1):
#             now = state
#             # print("state_start",state)
#             for line in range(1,lines):
#                 # print("line",line,1<=state-1<=n-1)
#                 if now == 1:
#                     # print("first")
#                     if visited[line][now]==True:
#                         now=now+1
#                 elif 1<now<n:
#                     # print("second")
#                     if visited[line][now]==True:
#                         # print("second-first")
#                         now=now+1
#                     elif visited[line][now-1]==True:
#                         # print("second-second")
#                         now = now-1
#                 else:
#                     # print("Trith")
#                     if visited[line][now-1]==True:
#                         now = now-1
#             #     print("move...",line,now)
#             # print("state_end",state,now)
#             if now != state:
#                 check="no"
#             if check == "no":
#                 return False
#         return True
#     lines+=1
#     visited = [[False]*(n+1) for _ in range(lines)]
#     for _ in range(r):
#         a,b = wow()
#         visited[a][b] = True
#     cnt = 100001
        
#     def go(y,x,count,visited,lines):
#         global cnt
#         global n
#         if check(visited):
#             if cnt > count:
#                 cnt = count
#             return
#         # print(y,x,"count",count)
#         # for i in visited[1:]:
#             # print(*i)
#         if count <3:
#             for state in range(x,n+1):
#                 for line in range(1,lines):
#                     if state == 1:
#                         if visited[line][state] == False:
#                             if visited[line][state+1] == False:
#                                 count+=1
#                                 visited[line][state]=True
#                                 go(line,state,count,visited,lines)
#                                 visited[line][state]=False
#                                 count-=1
#                     elif 1<state<n:
#                         if visited[line][state] == False:
#                             if visited[line][state-1]== False:
#                                 if visited[line][state+1]==False:
#                                     count+=1
#                                     visited[line][state]=True
#                                     go(line,state,count,visited,lines)
#                                     visited[line][state]=False
#                                 # if state-2 >=1:
#                                 #     if visited[line][state-2]== False:
#                                 #         visited[line][state-1]=True
#                                 #         go(line,state-1,count,visited,lines)
#                                 #         visited[line][state-1]=False
#                                     count-=1
#                     else:
#                         if visited[line][state-1] == False:
#                             if visited[line][state-2] == False:
#                                 count+=1
#                                 visited[line][state-1]=True
#                                 go(line,state,count,visited,lines)
#                                 visited[line][state-1]=False
#                                 count-=1 
#     go(1,1,0,visited,lines)
#     print(cnt if cnt <= 3 else -1)











