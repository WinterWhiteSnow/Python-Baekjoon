import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b = wow()
# print(a+b)

# print(1)

#https://www.acmicpc.net/problem/11000
# import heapq
# n_list = [list(wow()) for _ in range(one())]
# n_list.sort(key=lambda x: (x[0],x[1]))
# h = []
# end_time = 0
# for i in n_list:
#     a,b = i
#     if len(h) == 0:
#         h.append(b)
#     else:
#         if h[0] <=a:
#             heapq.heappop(h)
#             heapq.heappush(h,b)
#         else:
#             heapq.heappush(h,b)
#     # print(h)
# print(len(h))

#https://www.acmicpc.net/problem/2170
# n_list = [list(wow()) for _ in range(one())]
# n_list.sort(key=lambda x: (x[0],x[1]))
# start = []
# end = []
# for i in n_list:
#     a,b = i
#     if len(start) == 0:
#         start.append(a)
#         end.append(b)
#     else:
#         if end[0] >=a :
#             end[0]=max(b,end[0])
#         else:
#             check = "no"
#             for i in range(len(end)):
#                 if end[i]>=a:
#                     check ="yes"
#                     end[i]=b
#                     break
#             if check == "no":
#                 start.append(a)
#                 end.append(b)
#     # print(start,end)
# # print(start,end)
# cnt = 0
# for i in range(len(end)):
#     x,y = start[i],end[i]
#     cnt+=y-x
# print(cnt)

from collections import deque
l = one()
n_list = deque(list(wow()))
sorted_list = sorted(n_list)
cnt = 0
state = "none"
for num in range(1,l):
    # print("start",num)
    if num == 1:
        if n_list[0] == num:
            continue
        cnt+=1
        
    else:
        
    # print(cnt,n_list)
print(cnt)










