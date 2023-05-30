import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1660
# n = one()
# n_list = [1]
# total = 1
# plus = 2
# cnt = 1000000000000001
# while True:
#     total+=plus
#     a = total+n_list[-1]
#     if a > 300000:
#         break
#     n_list.append(a)
#     plus+=1
# start = len(n_list)-1
# def check(index,num,count):
#     # print("start!",index,num,count)
#     global cnt
#     if count >= cnt:
#         return
#     if num == 0:
#         # print("end!",count)
#         cnt = min(count,cnt)
#         return 
#     for m in range(index,-1,-1):
#         # print(m,n_list[m])
#         if num>=n_list[m]:
#             # print("wow",num,m,n_list[m])
#             check(m,num-n_list[m],count+1)
# check(start,n,0)
# print(cnt)

















