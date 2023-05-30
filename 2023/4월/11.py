import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/14002
# l = one()
# n_list = list(wow())
# total = [[0] for _ in range(l)]
# for i in range(l):
#     total[i]=[n_list[i]]
# max_l = 1
# index_index = 0
# for index in range(l):
#     for i in range(index): 
#         if n_list[index]>n_list[i]:
#             check = len(total[index])
#             if len(total[i])>= len(total[index]):
#                 total[index]=total[i]+[n_list[index]]
#                 if len(total[index]) > max_l:
#                     index_index = index
#                     max_l = len(total[index])
# print(max_l)
# print(*total[index_index])













