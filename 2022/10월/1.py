import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1036 36진수
# import string
# str_str = [str(i) for i in range(10)]+list(string.ascii_uppercase)
# n_dict = {}
# r = one()
# n_list = []
# for _ in range(r):
#     a = inputing()[::-1]
#     for index in range(len(a)):
#         if a[index] not in n_dict:
#             n_dict[a[index]]=35*(36**index)-((str_str.index(a[index]))*(36**index))
#         else:
#             n_dict[a[index]]+=35*(36**index)-((str_str.index(a[index]))*(36**index))
#     n_list.append(a)

# list_list = list(n_dict.items())
# list_list.sort(key= lambda x: x[1],reverse=True)
# # for i in list_list:
# #     print(i)
# list_list = list_list[:one()]
# key_list = [a for a,b in list_list]
# #역순인걸 기억하기
# for key in key_list:
#     for i in range(r):
#         n_list[i]=n_list[i].replace(key,"Z")
# cnt = 0
# for i in range(r):
#     a = n_list[i]
#     for index in range(len(a)):
#         cnt+=int(str_str.index(a[index]))*(36**index)

# new_list = []
# while cnt != 0:
#     answer = str_str[cnt%36]
#     new_list.append(answer)
#     cnt//=36
# # print(new_list)
# if len(new_list)>0:
#     print("".join(new_list[::-1]))
# else:
#     print(0)













