import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/6144
# r,k = wow()
# n_list = [0]*(k+1) #index = 무게, n_list[index] = 가치
# for i in range(1,r+1):
#     w,v = wow()
#     for kk in range(k,-1,-1):
#         if w>kk:
#             break
#         else:
#             n_list[kk]=max(n_list[kk],n_list[kk-w]+v)
# print(n_list[k])













