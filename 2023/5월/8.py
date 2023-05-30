import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1359
# from itertools import combinations
# n,m,k = wow()
# n_list = [i for i in range(1,n+1)]
# list_list = list(combinations(n_list,r=m))
# l = len(list_list)
# cnt = 0
# for a in list_list:
#     for b in list_list:
#         if len(set(a) & set(b))>=k:
#             cnt+=1
# print(cnt/(l*l))

























