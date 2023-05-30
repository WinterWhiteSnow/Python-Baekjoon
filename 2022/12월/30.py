import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/7696
# from collections import deque
# list_list = [i for i in range(1,10)]
# temp_list=deque(str(i) for i in range(1,10))
# index = 0
# check = "no"
# visited = [False]*10
# while True:
#     total = deque()
#     while len(temp_list) != 0:
#         a = temp_list.popleft()
#         new_list = deque()
#         visit = [i for i in visited]
#         for i in a:
#             visit[int(i)]=True
#         if set(visit) == {True}:
#             check = "yes"
#         for i in range(10):
#             n = str(i)
#             if visit[i]==False:
#                 c = [i for i in a]
#                 c.append(n)
#                 new_list.append(c)
#         for i in new_list:
#             num = int("".join(i))
#             list_list.append(num)
#             if len(list_list) == 1000000:
#                 check = "yes"
#                 break
#         if check == "yes":
#             break
#         total.extend(new_list)
#     if check == "yes":
#         break
#     temp_list=total
   
# list_list.sort()
# while True:
#     a = one()
#     if a == 0:
#         break
#     print(list_list[a-1])

for _ in range(one()):
    n_list = list(wow())























