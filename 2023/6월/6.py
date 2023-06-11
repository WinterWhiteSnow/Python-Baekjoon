import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/5525
# n = one()
# l = one()
# n_list = list(inputing())
# x,y=[0],[0]
# for i in range(0,l,2):
#     if n_list[i:i+3] == ["I","O","I"]:
#         x[-1]+=1
#     else:
#         x.append(0)
# for i in range(1,l,2):
#     if n_list[i:i+3] == ["I","O","I"]:
#         y[-1]+=1
#     else:
#         y.append(0)
# count = 0
# for i in x:
#     if i-n+1>0:
#         count+=i-n+1
# for i in y:
#     if i-n+1>0:
#         count+=i-n+1
# print(count)

#https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
# from collections import deque
# def solution(s):
#     answer = True
#     n_list = deque(list(s))
#     stack = []
#     while len(n_list)>0:
#         x = n_list.popleft()
#         if len(stack) == 0:
#             stack.append(x)
#         else:
#             if stack[-1]=="(":
#                 if x==")":
#                     stack.pop()
#                 else:
#                     stack.append(x)
#     # print("end",stack)
#     if len(stack)==0:
#         return True
#     else:
#         return False



        

    
















