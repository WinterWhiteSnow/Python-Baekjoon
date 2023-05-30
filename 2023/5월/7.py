import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15645
# r = one()
# max_max = list(wow())
# min_min = [i for i in max_max]
# for d in range(r-1):
#     a,b,c = wow()
#     new_max = [max(max_max[0],max_max[1])+a,max(max_max[0],max_max[1],max_max[2])+b,max(max_max[1],max_max[2])+c]
#     new_min = [min(min_min[0],min_min[1])+a,min(min_min[0],min_min[1],min_min[2])+b,min(min_min[1],min_min[2])+c]
#     max_max = new_max
#     min_min = new_min
# print(max(max_max),min(min_min))

#https://www.acmicpc.net/problem/13251
# r = one()
# n_list = list(wow())
# k = one()
# cnt = 0
# total = sum(n_list)
# count = 1
# for i in range(total,total-k,-1):
#     count*=i
# stack = 0
# for n in n_list:
#     if n>=k:
#         c = 1
#         for a in range(n,n-k,-1):
#             c*=a
#         stack+=c
# print(stack/count)












