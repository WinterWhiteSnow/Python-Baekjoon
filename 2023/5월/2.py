import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14607
# n = one()
# print(n*(n-1)//2)

#https://www.acmicpc.net/problem/4097
# while True:
#     r = one()
#     if r == 0:
#         break
#     n_list = [one() for _ in range(r)]
#     total = [-100001]*(r+1)
#     total[1]=n_list[0]
#     for i in range(2,r+1):
#         num = n_list[i-1]
#         # print(i,num)
#         total[i]=max(total[i-1]+num,num)
#     print(max(total))

for _ in range(one()):
    n = one()
    














