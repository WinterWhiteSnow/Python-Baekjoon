import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2225
# n,k = wow()
# n_list = [[0]*(n+1) for _ in range(k+1)]
# for i in range(n+1):
#     n_list[1][i]=1
# for i in range(2,k+1):
#     for c in range(n+1):
#         for minus in range(c+1):
#             n_list[i][c]+=n_list[i-1][c-minus]
#             n_list[i][c]%=1000000000
# print(n_list[k][n])

#합분해2
# n,k = wow()
# n_list = [[0]*(k+1) for _ in range(n+1)]
# for i in range(k+1):
#     n_list[1][i]=i
# for i in range(2,n+1):
#     for kk in range(k+1):
#         n_list[i][kk]=n_list[i-1][kk]+n_list[i][kk-1]
#         n_list[i][kk]%=1000000000
# print(n_list[n][k])

a = list(inputing())
b = inputing()
n_list = [[0]*(len(a)+1) for _ in range(len(b)+1)]
n_dict = {}
max_max = 0
for index in range(len(a)):
    for i in range(len(b)):
        if a[index]==b[i]:
            n_list[i][index]=1
       
for y in range(1,len(n_list)):
    for x in range(1,len(n_list[0])):
        n_list[y][x]+=max(n_list[y-1][x],n_list[y][x-1])
# for i in n_list:
#     print(i)
print(n_list[-1][-1])






