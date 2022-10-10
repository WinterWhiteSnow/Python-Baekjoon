import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1149
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# new_list = n_list[0]
# list_list = []
# for index in range(len(new_list)):
#     a = n_list[1][index]
#     state = index
#     x = (state+1)%len(new_list)
#     y = state-1
#     first = new_list[x]
#     second = new_list[y]
#     # print(x,y,first,second,a)
#     list_list.append(min(first,second)+a)
# new_list=list_list
# for index in range(2,r):
#     list_list = []
#     for i in range(3):
#         a = n_list[index][i]
#         state = i
#         x = (state+1)%len(new_list)
#         y = state-1
#         first = new_list[x]
#         second = new_list[y]
#         list_list.append(a+min(first,second))
#     new_list = list_list
# print(min(list_list))

#https://www.acmicpc.net/problem/1932
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# for i in range(r):
#     if i == 0:
#         pass
#     elif i == 1:
#         m_list = n_list[i]
#         for ii in range(len(m_list)):
#             n_list[i][ii]+=n_list[0][0]
#     else:
#         temp_list = n_list[i]
#         for index in range(len(temp_list)):
#             if index == 0 or index == len(temp_list)-1:
#                 if index == 0:
#                     n_list[i][index]+=n_list[i-1][index]
#                 else:
#                     n_list[i][index]+=n_list[i-1][index-1]
#             else:
#                 x = n_list[i-1][index-1]
#                 y = n_list[i-1][index]
#                 n_list[i][index]+=max(x,y)
# print(max(n_list[-1]))

#https://www.acmicpc.net/problem/11727
# num = one()
# zero_list = [0,1,3]
# if num <=2:
#     print(zero_list[num])
# else:
#     while len(zero_list) != num+1:
#         zero_list.append(((zero_list[-1])+(zero_list[-2])*2)%10007)
#     print(zero_list[num]%10007)

#https://www.acmicpc.net/problem/11279
# import heapq
# h = []
# for _ in range(one()):
#     a = one()
#     if a == 0:
#         if h:
#             print(-heapq.heappop(h))
#         else:
#             print(0)
#     else:
#         heapq.heappush(h,-a)
n_dict = {}
for i in range(1,10):
    n_dict[i]=1
n = one()
    








