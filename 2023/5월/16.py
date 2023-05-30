import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/27159
# l = one()
# n_list = list(wow())
# n_list.sort()
# state = []
# cnt = 0
# for i in range(l):
#     a = n_list[i]
#     if len(state) ==0:
#         state.append(a)
#     else:
#         if state[-1]+1 ==a:
#             state.append(a)
#         else:
#             cnt+=state[0]
#             state = [a]
#     # print(i,a,state,cnt)
# if len(state) != 0:
#     cnt+=state[0]
# print(cnt)

#https://www.acmicpc.net/problem/27960
# a,b = wow()
# print(a^b)

#https://www.acmicpc.net/problem/27465
# n = one()
# print(10**9)

#https://www.acmicpc.net/problem/27736
# a,b,c = 0,0,0
# total = 0
# l = one()
# n_list = list(wow())
# for i in range(l):
#     x = n_list[i]
#     if x == 1:
#         a+=1
#     if x == -1:
#         b+=1
#     if x == 0:
#         c+=1
#     total+=1
# if total/2 <=c:
#     print("INVALID")
# else:
#     if a>b:
#         print("APPROVED")
#     else:
#         print("REJECTED")

#https://www.acmicpc.net/problem/25801
# a = list(inputing())
# n_dict = {}
# for i in range(len(a)):
#     b = a[i]
#     if b not in n_dict:
#         n_dict[b]=1
#     else:
#         n_dict[b]+=1
# list_list = list(n_dict.values())
# state = "none"
# for n in list_list:
#     if state == "none":
#         state = n%2
#     else:
#         if state == n%2:
#             continue
#         else:
#             state ="0/1"
#             break
# print(state)


            
















