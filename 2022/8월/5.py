
import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 38 ㅋㅋ..
# import string
# a_list = list(string.ascii_uppercase)

# n_dict = {}
# l,many = inputing().split()
# n_list = list(inputing())
# for i in n_list:
#     if i not in n_dict:
#         n_dict[i] = 1
#     else:
#         n_dict[i]+=1
# list_list = sorted(list(n_dict.items()),key= lambda x : x[1],reverse=True)
# gap = a_list.index(list_list[0][0])-a_list.index(many)
# str_str = ""
# for i in n_list:
#     index = (a_list.index(i)-gap)%26
#     print(a_list[index],end="")

# import string
# a_list = list(string.ascii_letters)
# a_dict = {}
# str_str = ""
# for _ in range(one()):
#     str_str+=inputing().replace(" ","")
# for i in a_list:
#     a_dict[i]=str_str.count(i)
# list_list = [[a,b] for a,b in list(a_dict.items()) if b >= 1]
# for i in list_list:
#     print(*i)
# import string
# l = one()
# n_list = list(wow())
# a_list = list(string.ascii_uppercase)
# max_max = max(n_list)
# index_list = [a_list[i] for i in range(l) if n_list[i] == max_max]
# print("".join(index_list))

# l = one()
# n_list = inputing().split()
# cnt = 0
# zero_index = [i for i in range(l) if n_list[i] == "0"]
# # print(zero_index)
# max_index = l-1
# minus = len(zero_index)-1
# cnt = 0
# for i in zero_index:
#     cnt+=max_index-i-minus
#     minus-=1
# print(cnt)

# l = one()
# n_list = sorted(list(wow()))
# minus_list = [i for i in n_list if i < 0]
# plus_list = l-len(minus_list)
# cnt = plus_list*len(minus_list)+len(minus_list)*(len(minus_list)-1)
# print(cnt)
# while True:
#     a = one()
#     if a == 0:
#         break
#     n_list = [inputing() for _ in range(a)]
#     # 중복검사가 완전히 같아야 한다면
#     cnt = 0
#     while "" not in n_list:
#         n_list = [i[1:] for i in n_list]
#         count = 0
#         count="no"
#         cnt+=1
#         for i in n_list:
#             if n_list.count(i)>=2:
#                 count = "yes"
#                 break
#         if count == "yes":
#             break
#     print(cnt-1 if cnt>1 else 0)

# for _ in range(one()):
#     a = list(wow())
#     b = list(wow())
#     a = a[1:]
#     b = b[1:]
#     gap = 1000000
#     for x in a:
#         for y in b:
#             gap=min(abs(x-y),gap)
#     print(gap)

# for _ in range(one()):
#     a = inputing()
#     x = 0
#     y = 0
#     question = 0
#     for i in list(a):
#         if i == "U":
#             y+=1
#         if i == "R":
#             x+=1
#         if i == "D":
#             y-=1
#         if i == "L":
#             x-=1
#         if i == "?":
#             question+=1
#     print(x-question,y-question,x+question,y+question)
# import string
# a = inputing()
# gap = 0
# a_list = list(string.ascii_uppercase)
# while True:
#     gap+=1
#     str_str = ""
#     for i in list(a):
#         if i in a_list:
#             str_str+=a_list[(a_list.index(i)+gap)%len(a_list)]
#         else:
#             str_str+=i
#     if "CHIPMUNKS" in str_str:
#         print(str_str)
#         break
# a,b= wow()
# a = bin(a)[2:].zfill(16)
# b = bin(b)[2:].zfill(16)
# str_str = ""
# for x,y in zip(a,b):
#     str_str+=x
#     str_str+=y
# print(int(str_str,2))

# for _ in range(one()):
#     a = inputing().rstrip().lstrip()
#     if a.isdigit():
#         print(int(a))
#     else:
#         print("invalid input")

import math

print(21252-20*34/math.gcd(20,34)-325)









