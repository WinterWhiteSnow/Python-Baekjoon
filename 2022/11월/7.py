import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1935
# import string
# str_str = list(string.ascii_uppercase)
# r = one()
# n_list = inputing()
# str_list = []
# for i in n_list:
#     if i in str_str:
#         str_list.append(i)
# sort_list = sorted(list(set(str_list)))
# cnt = "none"
# n_dict = {}
# for i in range(r):
#     n_dict[sort_list[i]]=one()
# num_list = []
# symbol_list = []
# state = "none"
# for i in n_list:
#     if len(symbol_list) == 0:
#         if i in n_dict:
#             num_list.append(n_dict[i])
#         else:
#             symbol_list.append(i)
#     else:
#         if i not in n_dict:
#             symbol_list.append(i)
#         else:
#             number = n_dict[i]
#             for i in symbol_list:
#                 a,b = num_list.pop(),num_list.pop()
#                 a,b = b,a
#                 if i == "+":
#                     num_list.append(a+b)
#                 if i == "-":
#                     num_list.append(a-b)
#                 if i == "/":
#                     num_list.append(a/b)
#                 if i == "*":
#                     num_list.append(a*b)
#             symbol_list = []
#             num_list.append(number)
# for i in symbol_list:
#     a,b = num_list.pop(),num_list.pop()
#     a,b = b,a
#     if i == "+":
#         num_list.append(a+b)
#     if i == "-":
#         num_list.append(a-b)
#     if i == "/":
#         num_list.append(a/b)
#     if i == "*":
#         num_list.append(a*b)
# cnt = num_list[0]
# print(f"{cnt:.2f}")










