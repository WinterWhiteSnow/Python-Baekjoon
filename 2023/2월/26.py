import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17471
# from collections import deque
# n = one()
# n_list = list(wow())
# total = sum(n_list)
# connect = [[False]*(n) for _ in range(n)]
# for k in range(n):
#     m_list = list(wow())
#     num = m_list[0]
#     m_list = m_list[1:]
#     for x in range(num):
#         index = m_list[x]-1
#         connect[k][index]=True
#         connect[index][k]=True
#         # connect[k][k]=True
#         # connect[index][index]=True
# gap = 10000000000000000000000000000000000001
# from itertools import combinations
# check_list = deque()
# for index in range(1,n):
#     a = list(combinations([i for i in range(1,n+1)],r=index))
#     check_list.extend(a)
# # print(check_list)
# def check(first,visit):
#     global n
#     temp_list = deque()
#     temp_list.append(first[0])
#     cnt = 0
#     while temp_list:
#         index = temp_list.popleft()
#         if index in first:
#             visit[index]=True
#             cnt+=n_list[index]
#             for i in range(n):
#                 if connect[index][i]==True:
#                     if visit[i] == False:
#                         if i in first:
#                             visit[i]=True
#                             temp_list.append(i)
#     # print("check!!!",first,cnt,visit)
#     count = 0
#     for i in first:
#         if visit[i] == True:
#             count+=1
#     if len(first)==count:
#         return cnt
#     else:
#         return False
    
    
    
# def go(standard,visit):
#     global gap,n
#     cnt = 0
#     temp_list = deque()
#     temp_list.append(standard[0]-1)
#     while temp_list:
#         index = temp_list.popleft()
#         if index+1 in standard:
#             visit[index]=True
#             cnt+=n_list[index]
#             for i in range(n):
#                 if connect[index][i]==True:
#                     if visit[i] == False:
#                         if i+1 in standard:
#                             visit[i]=True
#                             temp_list.append(i)
#     # print(cnt,visit)
#     # print("Start",standard,cnt)
#     count = 0
#     for i in standard:
#         if visit[i-1] == True:
#             count+=1
#     if len(standard) == count:
#         list_list = deque()
#         for i in range(n):
#             if visit[i]==False:
#                 list_list.append(i)
#         answer = check(list_list,[False]*n)
#         if answer == False:
#             return
#         else:
#             # print("second",list_list)
#             # print(answer,cnt)
#             gap = min(gap,abs(answer-cnt))
#             # print("state!!!",gap)
#     else:
#         pass
# for standard in check_list:
#     go(standard,[False]*(n))
# print(gap if gap != 10000000000000000000000000000000000001 else -1)                           
    
        
    













