import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1495
# from collections import deque
# l,s,k = wow()
# n_list = list(wow())
# max_max = -1
# state = 0
# total = [[0]*(k+1) for _ in range(l+1)]
# if s <= k:
#     total[0][s]=1
# for i in range(1,l+1):
#     num = n_list[i-1]
#     for w in range(k+1):
#         if total[i-1][w]:
#             if w+num <= k:
#                 total[i][w+num]=1
#             if w-num>=0:
#                 total[i][w-num]=1
# for i in range(k,-1,-1):
#     if total[l][i]:
#         print(i)
#         exit()
# print(-1)



















