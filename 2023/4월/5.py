import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15990
# n_list = [[0,0,0] for _ in range(100001)]
# n_list[1][0]=1
# n_list[2][1]=1
# n_list[3][1]=1
# n_list[3][2]=1
# n_list[3][0]=1
# for i in range(4,100001):
#     n_list[i][0]=(n_list[i-1][1]+n_list[i-1][2])%1000000009
#     n_list[i][1]=(n_list[i-2][0]+n_list[i-2][2])%1000000009
#     n_list[i][2]=(n_list[i-3][0]+n_list[i-3][1])%1000000009
# for _ in range(one()):
#     n = one()
#     print(sum(n_list[n])%1000000009)

#https://www.acmicpc.net/problem/15991
# n_list = [0]*100001
# n_list[1]=1
# n_list[2]=2
# n_list[3]=2
# n_list[4]=3
# n_list[5]=3
# n_list[6]=6
# for i in range(7,100001):
#     n_list[i]=(n_list[i-2]+n_list[i-4]+n_list[i-6])%1000000009
# for _ in range(one()):
#     n = one()
#     print(n_list[n]%1000000009)

#https://www.acmicpc.net/problem/15992
# n_list = [[0]*1001 for _ in range(1001)]
# for i in range(1,1001):
#     n_list[i][i]=1
# n_list[1][1]=1
# n_list[3][1]=1
# n_list[3][2]=2
# n_list[2][1]=1
# for i in range(4,1001):
#     for r in range(2,i):
#         for n in [1,2,3]:
#             n_list[i][r]+=n_list[i-n][r-1]
#             n_list[i][r]%=1000000009
# for _ in range(one()):
#     a,b = wow()
#     print(n_list[a][b])

#https://www.acmicpc.net/problem/15993
# n_list = [[0,0] for _ in range(100001)]
# n_list[1][0]=0
# n_list[1][1]=1
# n_list[2][0]=1
# n_list[2][1]=1
# n_list[3][0]=2
# n_list[3][1]=2
# for i in range(4,100001):
#     for n in [1,2,3]:
#         n_list[i][0]+=n_list[i-n][1]
#         n_list[i][0]%=1000000009
#         n_list[i][1]+=n_list[i-n][0]
#         n_list[i][1]%=1000000009
# for _ in range(one()):
#     print(*n_list[one()][::-1])

#https://www.acmicpc.net/problem/16195
# n_list = [[0]*1001 for _ in range(1001)]
# for i in range(1,1001):
#     n_list[i][i]=1
# n_list[2][1]=1
# n_list[3][1]=1
# n_list[3][2]=2
# for i in range(4,1001):
#     for r in range(2,i):
#         for n in range(1,4):
#             n_list[i][r]+=n_list[i-n][r-1]
#             n_list[i][r]%=1000000009
# for _ in range(one()):
#     a,b = wow()
#     print(sum(n_list[a][:b+1])%1000000009)









