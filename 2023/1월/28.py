import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/8394
# n = one()
# if n == 1 :
#     print(0)
# else:
#     x,y = 2,3
#     if n==2:
#         print(x)
#     elif n == 3:
#         print(y)
#     else:
#         for _ in range(n-3):
#             x,y = y,x+y
#             x,y = x%10,y%10
#         print(y)

#https://www.acmicpc.net/problem/6236
# r,d = wow()
# n_list = [one() for _ in range(r)]
# start =1
# end = 10000*100000
# while start<=end:
#     mid = (start+end)//2
#     # print("Start!",mid)
#     now = mid
#     cnt = 0
#     for i in range(r):
#         x = n_list[i]
#         if now>=x:
#             now-=x
#         else:
#             cnt+=1
#             now = mid
#             if now>=x:
#                 now-=x
#             else:
#                 cnt = 100000
#                 break
#     if cnt >= d:
#         start = mid+1
#     else:
#         end = mid-1
# print(start)




















