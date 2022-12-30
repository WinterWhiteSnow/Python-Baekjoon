import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15965
# n_dict = {}
# for i in range(2,7500000):
#     if i not in n_dict:
#         for a in range(i,7500000,i):
#             n_dict[a]=0
#         n_dict[i]=1
# list_list = [a for a,b in n_dict.items() if b == 1]
# print(list_list[one()-1])

#https://www.acmicpc.net/problem/2477
# n_dict = {}
# list_list = []
# r = one()
# for _ in range(6):
#     a,b = wow()
#     list_list.append(b)
# total = 0
# x_index = 0
# y_index = 0
# for index in range(6):
#     x,y = list_list[index],list_list[(index+1)%len(list_list)]
#     if x*y > total:
#         x_index = index
#         y_index = (index+1)%len(list_list)
#         total = x*y
# # print(total,x_index,y_index)
# # print(list_list)
# a = (y_index+2)%len(list_list)
# b = (a+1)%len(list_list)
# print((total-list_list[a]*list_list[b])*r)















 






