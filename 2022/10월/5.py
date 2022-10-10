import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# import heapq
# https://www.acmicpc.net/problem/1202
# n,k = wow()
# h = []
# for _ in range(n):
#     heapq.heappush(h,list(wow()))
# k_list = [one() for _ in range(k)]
# k_list.sort()
# cnt = 0
# list_list = []
# for kk in k_list:
#     # print(kk,h)
#     for _ in range(len(h)):
#         if h[0][0]<=kk:
#             a,b = heapq.heappop(h)
#             heapq.heappush(list_list,-b)
#         else:
#             break
#     if list_list:
#         cnt-=heapq.heappop(list_list)
# print(cnt)

# l = one()
# t,p = wow()
# total = t*p
# n_list = sorted(list(wow()))
# if sum(n_list) < total:
#     print("STRESS")
# else:
#     cnt = 0
#     count = 0
#     while cnt < total:
#         cnt+=n_list.pop()
#         count+=1
#     print(count)
# cnt = 0
# count=0
# state = 0
# n_list = [list(wow()) for _ in range(11)]
# n_list.sort(key=lambda x: x[0])
# for i in n_list:
#     a,b = i
#     state+=a
#     cnt+=state
#     count+=b
    
# print(cnt+20*count)

import heapq
l,k = wow()
n_list = sorted(list(wow()))
cnt = 0
cnt+=n_list.count(10)
n_list = [i-(i%10) for i in n_list if i>10]
print(n_list)
for _ in range(k):
    if n_list:
        if a>=10:
            cnt+=1
            a-=10
        if a == 10:
            cnt+=1
        elif a > 10:
            heapq.heappush(n_list,a)
        else:
            pass
    else:
        break
print(cnt)        









