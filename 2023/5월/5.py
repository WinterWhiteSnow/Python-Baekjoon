import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10164
# r,l,k = wow()
# n_list = [i for i in range(1,r*l+1)]
# new_list = []
# for i in range(0,l*r,l):
#     new_list.append(n_list[i:i+l])
# total = [[0]*l for _ in range(r)]
# if l > 1:
#     total[0][1]=1
# if r > 1:
#     total[1][0]=1
# def go(y,x):
#     cnt = total[y][x]
#     if 0<=y-1:
#         cnt+=total[y-1][x]
#     if 0<=x-1:
#         cnt+=total[y][x-1]
#     return cnt
# for y in range(r):
#     for x in range(l):
#         a = go(y,x)
#         if new_list[y][x] == k:
#             total = [[0]*l for _ in range(r)]
#         total[y][x]=a
# total[0][0]=1
# print(total[-1][-1])

#https://www.acmicpc.net/problem/1446
# r,k = wow()
# n_list = [i for i in range(k+1)]
# num_list = [list(wow()) for _ in range(r)]
# num_list.sort(key=lambda x: x[1])
# for a,b,v in num_list:
#     if b<=k:
#         front = n_list[b]
#         n_list[b]=min(n_list[b],n_list[a]+v)
#         # print(a,b,n_list[b])
#         if front > n_list[b]:
#             for i in range(b+1,k+1):
#                 n_list[i]=min(n_list[i],n_list[i-1]+1)
#         # print(n_list[b])
# print(n_list[k])

from itertools import combinations
n_list = [1]
print(1,1)
for n in range(2,50):
    n_list.append(n)
    cnt = 0
    for i in range(1,n):
        list_list = list(combinations(n_list,r=i))
        # print(n,[i for i in list_list if sum(i) == n])
        cnt+=len([i for i in list_list if sum(i) == n])
    print(n,cnt)
# total = [1]*2001
# total[1]=1
# total[3]=2
# for i in range(4,2001):
#     total[i]=(total[i-2]+total[i-3])%100999
# for _ in range(one()):
#     print(total[one()])








