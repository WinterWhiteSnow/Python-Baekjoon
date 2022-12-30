import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/13908
# total = [0]
# l,know = wow()
# n_list = list(wow())
# def go(list_list,l,check_list):
#     if len(list_list) != l:
#         for i in range(10):
#             temp_list = [i for i in list_list]
#             temp_list.append(i)
#             go(temp_list,l,check_list)
#     else:
#         check = "yes"
#         for i in check_list:
#             if i in list_list:
#                 continue
#             check = "no"
#             break
#         if check == "yes":
#             total[0]+=1
# go([],l,n_list)
# print(total[0])
















