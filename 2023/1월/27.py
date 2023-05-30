import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14494
# x,y = wow()
# n_list = [[0]*x for _ in range(y)]
# n_list[0]=[1]*x
# for i in range(y):
#     n_list[i][0]=1
# for y_index in range(1,y):
#     for x_index in range(1,x):
#         n_list[y_index][x_index]+=n_list[y_index-1][x_index]
#         n_list[y_index][x_index]+=n_list[y_index][x_index-1]
#         n_list[y_index][x_index]+=n_list[y_index-1][x_index-1]
#         n_list[y_index][x_index]%=1000000007
#         # print("wow")
#         # for i in n_list:
#         #     print(*i)
# print(n_list[y-1][x-1])


















