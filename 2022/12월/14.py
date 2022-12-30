import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1406
# from collections import deque
# left = deque(inputing())
# right = deque()
# for _ in range(one()):
#     order = inputing().split()
#     a = order[0]
#     if a== "L":
#         if len(left) > 0:
#             right.appendleft(left.pop())
#     elif a == "D":
#         if len(right)>0:
#             left.append(right.popleft())
#     elif a == "B":
#         if len(left)>0:
#             left.pop()
#     else:
#         a,b = order
#         left.append(b)
#         move = len(left)
#     # print("left",left)
#     # print("right",right)
# print("".join(left+right)) 

#https://www.acmicpc.net/problem/2504
# from collections import deque
# n_list = list(inputing())
# stack = []
# cnt = 0
# state = "none"
# check = "yes"
# list_list = []
# number_list = []
# for i in n_list:
#     if i == "(" or i == "[":
#         if state != "none":
#             stack.append(str(state))
#             state = "none"
#         stack.append(i)
#     else:
#         if i == ")":
#             if len(stack) > 0:
#                 if stack[-1] == "(":
#                     stack.pop()
#                     if state == "none":
#                         state = 2
#                     else:  
#                         state*=2 
#                 else:       
#                     while stack[-1].isdigit():
#                         state+=int(stack.pop())
#                         if len(stack) == 0:
#                             break
#                     if len(stack) > 0:
#                         if stack[-1] == "(":
#                             stack.pop()
#                             if state == "none":
#                                 state = 2
#                             else:
#                                 state*=2
#                         else:
#                             check ="no"
#                             break
#                     else:
#                         check ="no"
#                         break
#             else:
#                 check ="no"
#                 break
#         else:
#             if len(stack) > 0:
#                 if stack[-1] == "[":
#                     stack.pop()
#                     if state == "none":
#                         state = 3
#                     else:
#                         state*=3
#                 else:
#                     while stack[-1].isdigit():
#                         state+=int(stack.pop())
#                         if len(stack) == 0:
#                             break
#                     if len(stack)>0:
#                         if stack[-1] == "[":
#                             stack.pop()
#                             if state == "none":
#                                 state = 3
#                             else:
#                                 state*=3
#                         else:
#                             check ="no"
#                             break
#                     else:
#                         check ="no"
#                         break
#             else:
#                 check = "no"
# #     print(i,stack,state)
# # print(check)
# if check == "no":
#     print("0")
# else:
#     if "(" in stack or "[" in stack:
#         print(0)
#     else:
#         if state != "none":
#             cnt+=state
#         while len(stack) > 0:
#             cnt+=int(stack.pop())
#         print(cnt)

from collections import deque
l = one()
n_list = list(wow())
stack = deque()
state = "none"
state_list = []
while len(n_list)!=0:
    a = n_list.pop()
    # print(n_list,a)
    if state == "none":
        state=a
    else:
        if a < state:
            if len(n_list)>0:
                b=n_list[-1]
                if b<a:
                    stack.appendleft(state)
                    state_list.append(state)
                    state = a
                else:
                    stack.appendleft(state)
            else:
                stack.appendleft(state)
        else:
            if len(n_list) == 0:
                # print(n_list,a)
                index = "none"
                for i in stack:
                    # print(i,i>a)
                    if i > a and i != -1:
                        index = i
                        break
                # print("wow!!",i,i>a)
                if index != "none":
                    stack.appendleft(index)
                else:
                    stack.appendleft(-1)
            else:
                state_list.append(state)
                state = a
                index = "none"
                for i in state_list:
                    if i > a and index == "none":
                        index= i
                    else:
                        if i>a:
                            index=min(index,i)
                if index != "none":
                    stack.appendleft(index)
                    state = index
                else:
                    stack.appendleft(-1)
    print(stack,a,state)
    print(state_list)
stack.append(-1)
print(*stack)
        








    

    












