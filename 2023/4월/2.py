import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1309
# r = one()
# n_list = [[0,0,0] for _ in range(r)]
# n_list[0][0]=1 # ox
# n_list[0][1]=1 # xo
# n_list[0][2]=1 # xx
# for  i in range(1,r):
#     n_list[i][0] = (n_list[i-1][1]+n_list[i-1][2])%9901
#     n_list[i][1] = (n_list[i-1][0]+n_list[i-1][2])%9901
#     n_list[i][2] = (n_list[i-1][0]+n_list[i-1][1]+n_list[i-1][2])%9901
# print(sum(n_list[r-1])%9901)



        
    
    














