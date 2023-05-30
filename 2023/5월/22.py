import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1527
# cnt = 0
# a,b = wow()
# def check(str_str):
#     global cnt
#     # print("start!",str_str)
#     if int(str_str)>b:
#         return
#     if a<=int(str_str)<=b:
#         cnt+=1
#     for n in "47":
#         check(str_str+n)
# check("0")
# print(cnt)

#https://www.acmicpc.net/problem/1107
# n = one()
# start = 100
# l = one()
# gap = abs(n-start)
# v = [0]*10
# def check(str_str,l):
#     global n,gap
#     if l-1<=len(str_str)<=l+1:
#         if len(str_str)==0:
#             pass
#         else:
#             count = 0
#             count = min(abs(int(str_str)-100),len(str_str))
#             count+=abs(n-int(str_str))
#             gap = min(gap,count)
#     if len(str_str)<=l:
#         for i in range(10):
#             if v[i]==1:
#                 continue
#             check(str_str+str(i),l) 
# if l != 0:
#     l = len(str(n))
#     n_list = list(wow())
#     for a in n_list:
#         v[a]=1
# check("",len(str(n)))
# print(gap)














