import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15828
# from collections import deque
# limit = one()
# stack = deque()
# while True:
#     a = one()
#     if  a==-1:
#         break
#     if a == 0:
#         if len(stack)>0:
#             stack.popleft()
#     else:
#         if len(stack) < limit:
#             stack.append(a)
#     print(stack)
# print(*stack if len(stack) > 0 else "empty")

#https://www.acmicpc.net/problem/14713
# from collections import deque
# n_list = deque()
# n_dict = {}
# for i in range(one()):
#     n_dict[i]=deque(inputing().split())
# a_list = deque(inputing().split())
# check ="yes"
# while len(a_list) > 0:
#     a = a_list.popleft()
#     check = "no"
#     for key in n_dict.keys():
#         if len(n_dict[key])>0:
#             if n_dict[key][0] == a:
#                 n_dict[key].popleft()
#                 check = "yes"
#                 break
#     if check == "no":
#         a_list.appendleft(a)
#         break
# # print(a_list)
# # print(n_dict)
# num = sum(list(map(len,list(n_dict.values()))))
# print("Possible" if len(a_list)==0 and num == 0 else "Impossible")


        
            
        
                
    











