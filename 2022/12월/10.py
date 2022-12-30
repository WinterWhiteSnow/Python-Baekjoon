import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/24444
#https://www.acmicpc.net/problem/24445
# from collections import deque
# n,r,start = wow()
# n_dict = {}
# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         n_dict[b]+=[a]
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key],reverse=True)
# visited = [False]*(n+1)
# list_list = []
# queue = deque()
# while True:
#     if len(list_list) == 0:
#         visited[start]=True
#         list_list.append(start)
#         if start in n_dict:
#             queue.extend(n_dict[start])
#     else:
#         while len(queue) != 0:
#             index = queue.popleft()
#             # print(queue)
#             # print(list_list)
#             if visited[index] == False:
#                 visited[index]=True
#                 list_list.append(index)
#                 if index in n_dict:
#                     queue.extend(n_dict[index])
#         break
# zero_list = [0]*(n+1)
# for a,b in enumerate(list_list):
#     zero_list[b]=a+1
# print(*zero_list[1:],sep="\n")

#https://www.acmicpc.net/problem/24446
#https://www.acmicpc.net/problem/24447
# from collections import deque
# n,r,start = wow()
# n_dict = {}
# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         n_dict[b]+=[a]
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key])
# # print(n_dict)
# visited = [False]*(n+1)
# list_list = []
# queue = deque()
# depth = [-1]*(n+1)
# number = 0
# while True:
#     new_list = []
#     if visited[start] == False:
#         visited[start]=True
#         list_list.append(start)
#         depth[start]=number
#         number+=1
#         if start in n_dict:
#             new_list.extend(n_dict[start])
#     else:
#         if len(queue) == 0:
#             break
#         tem_list = deque(queue.popleft())
#         # print("start",tem_list)
#         # print("number",number)
#         check = "no"
#         while len(tem_list) != 0:
#             index = tem_list.popleft()
#             # print(queue)
#             # print(list_list)
#             if visited[index] == False:
#                 check = "yes"
#                 visited[index]=True
#                 depth[index]=number
#                 list_list.append(index)
#                 if index in n_dict:
#                     new_list.extend(n_dict[index])
#         if check == "yes":
#             number+=1
#     if len(new_list) > 0:
#         queue.append(new_list)
#         # print("number",number)
#     # print(depth)
#     # print(queue)
# zero_list = [0]*(n+1)
# for a,b in enumerate(list_list):
#     zero_list[b]=a+1
# depth = depth[1:]
# zero_list = zero_list[1:]
# cnt = 0
# # print(zero_list)
# # print(depth)
# for a,b in zip(zero_list,depth):
#     cnt+=a*b
# print(cnt)

#https://www.acmicpc.net/problem/2659
# from collections import deque
# n_list = deque(inputing().split())
# n_list_list = ["".join((n_list))]
# for _ in range(3):
#     n_list.rotate(1)
#     n_list_list.append("".join(n_list))
# n_list_list.sort()
# n_list = "".join(n_list_list[0])
# # print(n_list)
# start="1111"
# index = 1
# n_dict= {}
# while n_list not in n_dict:
#     check = "no"
#     while True:
#         if "0" not in start:
#             temp_list = deque([i for i in list(start)])
#             new_list = ["".join(temp_list)]
#             for _ in range(3):
#                 temp_list.rotate(1)
#                 new_list.append("".join(temp_list))
#             new_list.sort()
#             str_str = "".join(new_list[0])
#             if str_str not in n_dict:
#                 check = "yes"
#                 break
#         start=str(int(start)+1)
#     if check == "yes":
#         n_dict[str_str]=index
#         index+=1
#     # print(n_dict)
# print(n_dict[n_list])

#https://www.acmicpc.net/problem/1485
# for _ in range(one()):
#     list_list = []
#     for _ in range(4):
#         x,y = wow()
#         list_list.append([x,y])
#     list_list.sort(key=lambda x: (x[0],x[1]))
#     l = []
#     for i in range(1,3):
#         for ii in [0,3]:
#             x,y = list_list[i]
#             a,b = list_list[ii]
#             if ii == 0:
#                 l.append(((x-a)**2+(y-b)**2)**(1/2))
#             else:
#                 l.append(((a-x)**2+(b-y)**2)**(1/2))
#     # print(l)
#     if len(set(l)) == 1:
#         check = []
#         a,b = list_list[0]
#         x,y = list_list[3]
#         check.append(((x-a)**2+(y-b)**2)**(1/2))
#         a,b = list_list[1]
#         x,y = list_list[2]
#         check.append(((x-a)**2+(y-b)**2)**(1/2))
#         if len(set(check)) == 1:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(0)

import math
r,l= wow()
n_list = [list(wow()) for _ in range(r)]
n_list.sort(key=lambda x: x[0])

    










