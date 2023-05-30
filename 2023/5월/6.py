import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/22971
# l = one()
# n_list = list(wow())
# total = [1]*l
# for i in range(1,l):
#     num = n_list[i]
#     for a in range(i):
#         if n_list[a]<num:
#             total[i]+=total[a]
#             total[i]%=998244353
# print(*total)

#https://www.acmicpc.net/problem/17213
# n = one()
# r = one()-n
# cnt = 1
# for i in range(r+n-1,n-1,-1):
#     cnt*=i
# for i in range(2,r+1):
#     cnt//=i
# print(cnt)

total = [0]*(2001)
total[1]=1
total[2]=1
total[3]=2
total[4]=2
total[5]=4
total[6]=4











