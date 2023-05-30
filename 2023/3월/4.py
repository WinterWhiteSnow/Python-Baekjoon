import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/17135
# from collections import deque
# n,m,d = wow()
# n_list = [list(wow()) for _ in range(n)]
# n_list = deque(n_list)
# visit = [False]*m
# move = [(0,-1),(1,0),(-1,0),(0,1)]
# front = [0]*m
# cnt = 0
# def check(y_index,x_index,m_list):
#     global m,n,d
#     # print("start!!!!",y_index,x_index)
#     visited = [[False]*m for _ in range(n)]
#     list_list = []
#     q = deque()
#     q.append((y_index,x_index))
#     for dd in range(d):
#         # print(dd)
#         # print("q",q)
#         temp_list = deque()
#         while q:
#             y,x = q.popleft()
#             # print("for 이전",y,x,"현재q",q)
#             for index in range(4):
#                 yy,xx= move[index]
#                 yyy,xxx = y+yy,x+xx
#                 # print(yyy,xxx)
#                 if 0<=yyy<n and 0<=xxx<m:
#                     # print("통과!!!",yyy,xxx)
#                     if visited[yyy][xxx] == False:
#                         visited[yyy][xxx]=True
#                         # print("what?",n_list[yyy][xxx])
#                         if m_list[yyy][xxx]:
#                             list_list.append((yyy,xxx))
#                             break
#                         temp_list.append((yyy,xxx))
#             if list_list:
#                 break
#         if list_list:
#             break
#         q= temp_list
#     if list_list:
#         return list_list.pop()
#     else:
#         return False
# def go(count):
#     global m,n,cnt
#     if count < 3:
#         for i in range(m):
#             if visit[i]== False:
#                 visit[i]=True
#                 go(count+1)
#                 visit[i]=False
#     else:
#         # print(visit,count)
#         # visit = [True,False,True,False,True]
#         index_list = []
#         for i in range(m):
#             if visit[i]:
#                 index_list.append((n,i))
#         count = 0
#         m_list = deque()
#         for i in n_list:
#             kk = []
#             for a in i:
#                 kk.append(a)
#             m_list.append(kk)
#         # print("Start!!!")
#         # print(*m_list,sep="\n")
#         for nn in range(n):
#             wait = []
#             for y_index,x_index in index_list:
#                 a = check(y_index,x_index,m_list)
#                 if not a:
#                     continue
#                 wait.append(a)
#             # if visit == [True,False,True,False,True]:
#             #     print("wat",wait)
#             for yy,xx in wait:
#                 if m_list[yy][xx]:
#                     m_list[yy][xx]=0
#                     count+=1
#             # if nn < 2:
#             #     print(wait)
#             #     print("nn",nn,count,visit)
#             #     print(*m_list,sep="\n")
#             m_list.pop()
#             m_list.appendleft(front)
#             # if visit == [True,False,True,False,True]:
#             #     print("now!")
#             #     print(*n_list,sep="\n")
#         # exit()
#         # print(visit,count)
#         if cnt < count:
#             # print("now",count)
#             # print(*m_list,sep="\n")
#             cnt = count
# for i in range(m):
#     visit[i]=True
#     go(1)
#     visit[i]=False
# # go(3)
# print(cnt)

#돌게임6
# n = one()
# n-=1
# n%=7
# if n==1 or n == 6:
#     print("CY")
# else:
#     print("SK")

#https://www.acmicpc.net/problem/9661
# n = one()-1
# n%=5
# if n==1 or n==4:
#     print("CY")
# else:
#     print("SK")













