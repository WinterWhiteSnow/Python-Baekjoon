import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/10432
# for _ in range(one()):
#     n_list = list(wow())
#     num = n_list[0]
#     n_list=n_list[1:]
#     stack = []
#     temp=[]
#     state = 0
#     cnt = 0
#     if len(stack) == 0:
#         for i in n_list:
#             if state < i:
#                 temp.append(i)
#             else:
#                 if len(temp)>0:
#                     stack.append(temp)
#                     temp=[]
#                     cnt+=1
#     # print(stack)
#     while len(stack)>0:
#         list_list = stack.pop()
#         # print(list_list)
#         state = min(list_list)
#         temp = []
#         for i in list_list:
#             if i>state:
#                 temp.append(i)
#             else:
#                 if len(temp)>0:
#                     stack.append(temp)
#                     temp=[]
#                     cnt+=1
#         if len(temp)>0:
#             stack.append(temp)
#             cnt+=1
#     print(num,cnt)


















            



















