import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3#
#힙에서 특정값(최대값)을 빼오는건 인덱싱을 하는것과 동일하고, 최소값을 손쉽게 빼는것말고는 다른 능력이 없음...
# import heapq
# def solution(operations):
#     n_list = operations
#     h = []
#     for i in n_list:
#         order,num=i.split()
#         num = int(num)
#         a,b = num,-num
#         if order == "I":
#             heapq.heappush(h,num)
#         else:
#             if num == 1:
#                 temp_list = []
#                 while h:
#                     heapq.heappush(temp_list,-heapq.heappop(h))
#                 if temp_list:
#                     heapq.heappop(temp_list)
#                 while temp_list:
#                     heapq.heappush(h,-heapq.heappop(temp_list))
#             else:
#                 if h:
#                     heapq.heappop(h)
#     if len(h)==1:
#         a = h.pop()
#         return [a,a]
#     else:
#         if h:
#             min_min = heapq.heappop(h)
#         else:
#             min_min = 0
#         if h:
#             temp_list = []
#             while h:
#                 heapq.heappush(temp_list,-heapq.heappop(h))
#             max_max = -heapq.heappop(temp_list)
#         else:
#             max_max = 0
#         return [max_max,min_min]

#https://www.acmicpc.net/problem/9996
# r = one()
# str_str = inputing()
# str_l = len(str_str)
# str_str = str_str.split("*")
# x,y = str_str
# xx,yy = len(x),len(y)
# cnt = 0
# for _ in range(r):
#     a = inputing()
#     # print(a[:xx],x,a[-yy:],y,type(a[:xx]),type(x))
#     if a[:xx]==x:
#         a=a[xx:]
#         if a[-yy:]==y:
#             print("DA")
#         else:
#             print("NE")
#     else:
#         print("NE")






















