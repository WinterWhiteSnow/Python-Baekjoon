import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/5397
# from collections import deque
# for _ in range(one()):
#     str_str = list(inputing())
#     right = deque()
#     left = deque()
#     for order in str_str:
#         if order == "<":
#             if len(left)>0:
#                 right.appendleft(left.pop())
#         elif order == ">":
#             if len(right)>0:
#                 left.append(right.popleft())
#         elif order == "-":
#             if len(left)>0:
#                 left.pop()
#         else:
#             left.append(order)
#     print("".join(left+right))

#자료구조는 정말 최고야
# from collections import deque
# n,r = wow()
# check = "yes"
# for _ in range(r):
#     l = one()
#     n_list = deque(wow())
#     for i in range(l-1):
#         if n_list[i]<n_list[i+1]:
#             check = "no"
#             break
#     if check == "no":
#         break
# print("Yes" if check == "yes" else "No")
            
#https://www.acmicpc.net/problem/15815
# from collections import deque
# str_str = deque(inputing())
# stack = deque()
# for i in str_str:
#     if i.isdigit():
#         stack.append(int(i))
#     else:
#         a,b = stack.pop(),stack.pop()
#         if i == "+":
#             stack.append(a+b)
#         if i == "*":
#             stack.append(a*b)
#         if i == "/":
#             stack.append(b//a)   
#         if i == "-":
#             stack.append(b-a)
#     # print(stack)
# print(*stack)


























