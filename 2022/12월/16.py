import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/2257
# from collections import deque
# stack = deque()
# for i in inputing():
#     if i.isdigit():
#         if stack[-1] == ")":
#             str_str = ""
#             stack.pop()
#             while stack[-1] != "(":
#                 str_str+=stack.pop()
#             stack.pop()
#             str_str*=int(i)
#             for x in str_str:
#                 stack.append(x)
#         else:
#             a = stack.pop()*int(i)
#             for x in a:
#                 stack.append(x)
#     else:
#         if len(stack) > 0:
#             if stack[-1] == ")":
#                 stack.pop()
#                 str_str = ""
#                 while stack[-1] != "(":
#                     str_str+=stack.pop()
#                 stack.pop()
#                 for x in str_str:
#                     stack.append(x)   
#         stack.append(i)
#     # print(stack)
# cnt = 0
# for i in stack:
#     if i == "H":
#         cnt+=1
#     if i == "C":
#         cnt+=12
#     if i == "O":
#         cnt+=16
# print(cnt)

#https://www.acmicpc.net/problem/2304
# from collections import deque
# n_list = []
# for _ in range(one()):
#     n_list.append(list(wow()))
# n_list.sort(key=lambda x: x[0])
# max_max = 0
# max_index = 0
# for i in range(len(n_list)):
#     a,b = n_list[i]
#     if max_max < b:
#         max_max=b
#         max_index=i

# left = deque(n_list[:max_index])
# right = deque(n_list[max_index:][::-1])
# def go(list_list):
#     for i in range(1,len(list_list)):
#         a,b = list_list[i]
#         x,y = list_list[i-1]
#         if b<y:
#             list_list[i][1]=y
#     return list_list
# left = go(left)
# right =go(right)
# left.append(right[-1])
# # print(left)
# # print(right)
# cnt = 0
# for i in range(1,len(left)):
#     a,b = left[i]
#     x,y = left[i-1]
#     cnt+=(a-x)*y
# for i in range(1,len(right)):
#     a,b = right[i]
#     x,y = right[i-1]
#     cnt+=(x-a)*y
# print(cnt+max_max)

#https://www.acmicpc.net/problem/5002
# from collections import deque
# gap = one()
# m = 0
# w = 0
# n_list = deque(inputing())
# # print(len(n_list))
# while len(n_list) > 1:
#     a,b = n_list.popleft(),n_list.popleft()
#     mm = m
#     ww = w
#     if a==b:
#         if a == "M":
#             mm+=1
#         else:
#             ww+=1
#         if abs(mm-ww)>gap:
#             break
#         n_list.appendleft(a)
#     else:
#         if a == "M":
#             mm+=1
#         else:
#             ww+=1
#         if abs(mm-ww)>gap:
#             if a == "M":
#                 mm-=1
#                 ww+=1
#             else:
#                 ww-=1
#                 mm+=1
#             n_list.appendleft(a)
#             if abs(mm-ww)>gap:
#                 n_list.appendleft(b)
#                 break
#         else:
#             n_list.appendleft(b)
#     m=mm
#     w=ww
#     # print(n_list,len(n_list))
#     # print(m,w)
# if len(n_list) == 1:
#     a = n_list.pop()
#     mm = m
#     ww = w
#     if a == "M":
#         mm+=1
#     else:
#         ww+=1
#     if abs(mm-ww)<=gap:
#         m=mm
#         w=ww
# # print(n_list)
# print(m+w)



        












