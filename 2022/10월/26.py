import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/23827
# l = one()
# n_list = list(wow())
# zero_list = []
# for i in range(l):
#     if len(zero_list) == 0:
#         zero_list.append((sum(n_list[1:])%1000000007))
#     else:
#         zero_list.append((zero_list[-1]-n_list[i])%1000000007)
# cnt = 0    
# for i in range(l):
#     cnt+=(zero_list[i]*n_list[i]%1000000007)
# print(cnt%1000000007)

#https://www.acmicpc.net/problem/13116
# for _ in range(one()):
#     a,b = wow()
#     b_list = []
#     if a>b:
#         a,b = b,a
#     while b != 1:
#         if b%2:
#             b-=1
#             b//=2
#         else:
#             b//=2
#         b_list.append(b)
#     if a in b_list:
#         print(a*10)
#     else:
#         while a != 1:
#             if a%2:
#                 a-=1
#                 a//=2
#             else:
#                 a//=2
#             if a in b_list:
#                 break
#         print(a*10)

#https://www.acmicpc.net/problem/15725
# n_list = inputing()
# if "x" in n_list:
#     x_index = n_list.index("x")
#     str_str = ""
#     symbol = "none"
#     for i in range(x_index-1,-1,-1):
#         # print(n_list[i])
#         if n_list[i].isdigit():
#             str_str+=n_list[i]
#         else:
#             if n_list[i] == "-" or n_list[i] == "+":
#                 symbol=n_list[i]
#                 break
#     if str_str == "":
#         str_str = "1"
#     str_str=str_str[::-1]
#     if symbol =="-":
#         print(symbol+str_str)
#     else:
#         print(str_str)
# else:
#     print(0)

n = one()
n_list = [1]*(n+1)
l = n+1
for i in range(1,n+1):
    for a in range(i,len(n_list),i):
        n_list[a] = not n_list[a]
n_list=n_list[1:]
print(n_list.count(False))












