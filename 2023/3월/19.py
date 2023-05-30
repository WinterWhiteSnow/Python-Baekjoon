import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2195
# a = inputing()
# b = deque(inputing())
# index = 0
# stack = ""
# cnt = 0
# while b:
#     x = b.popleft()
#     if stack+x in a:
#         stack+=x
#     else:
#         cnt+=1
#         stack=x
# #     print(cnt,stack)
# # print(stack)
# if stack:
#     cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/2885
# k = one()
# time = 0
# index = 0
# while 2**index <k:
#     index+=1
# total = 2**index
# if k == total:
#     print(total,0)
# else:
#     count = 0
#     while k>count:
#         if count+total//2 <=k:
#             count+=total//2
#         total//=2
#         time+=1
#     # print(count)
#     print(2**index,time)

l,limit = wow()
n_list = sorted(list(wow()))
print(n_list)










