import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/18222
# num = one()
# if num == 1:
#     print(0)
# else:
#     number = 1
#     index = 1
#     list_list = []
#     count = 0
#     while number < num:
#         number*=2
#         count+=1
#     list_list = [num]
#     def go(num,goal):
#         index = abs(num//2-goal)
#         cnt = 2
#         # print(goal,num,index)
#         list_list.append(index)
#         while cnt < index:
#             cnt*=2
#         if index >= 2:
#             go(cnt,index)
#     go(number,num)
#     # print(list_list)
#     print(0 if len(list_list)%2 else 1)
    














