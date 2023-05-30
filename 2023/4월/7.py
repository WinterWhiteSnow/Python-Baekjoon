import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/12865
# r,k = wow()
# n_list = [0]+[list(wow()) for _ in range(r)]
# zero_list = [[0]*(k+1) for _ in range(r+1)]
# for index in range(1,r+1):
#     weigt,value = n_list[index]
#     for w in range(1,k+1):
#         if weigt > w:
#             zero_list[index][w]=zero_list[index-1][w]
#         else:
#             zero_list[index][w]=max(zero_list[index-1][w],zero_list[index-1][w-weigt]+value)
# print(zero_list[r][k])


l,k = wow()
a_list = list(wow())
b_list = list(wow())







