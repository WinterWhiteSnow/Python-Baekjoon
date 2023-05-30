import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2302
# num_list = [0]*(40+1)
# num_list[1]=1
# num_list[0]=1
# num_list[2]=2
# for i in range(3,41):
#     num_list[i]=num_list[i-1]+num_list[i-2]
# n = one()
# c = one()
# n_list = [one() for _ in range(c)]
# v = [0]*n
# for i in n_list:
#     v[i-1]=1
# # print(num_list)
# r=0
# cnt = 1
# for i in range(n):
#     if v[i]==0:
#         r+=1
#     else:
#         # print("now,",i,num_list[r])
#         cnt*=num_list[r]
#         r=0
#     # print(i,cnt)
# cnt*=num_list[r]
# print(min(cnt,2000000000))

#https://www.acmicpc.net/problem/15989

n_list = [[0,0,0,0] for _ in range(10001)]
for i in range(10001):
    n_list[i][1]=1
n_list[2][2]=1
n_list[3][2]=1
n_list[3][3]=1
for i in range(4,10001):
    n_list[i][2]=n_list[i-2][2]+n_list[i-2][1]
    n_list[i][3]=n_list[i-3][3]+n_list[i-3][2]+n_list[i-3][1]
for _ in range(one()):
    n = one()
    print(sum(n_list[n]))
    
    
    









        
















