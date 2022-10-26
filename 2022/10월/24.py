import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2485
# import math
# l = one()
# n_list = [one() for _ in range(l)]
# n_list.sort()
# gap_list = []
# for i in range(1,l):
#     gap_list.append(n_list[i]-n_list[0])
# while len(gap_list) != 1:
#     a,b = gap_list.pop(),gap_list.pop()
#     gap_list.append(math.gcd(a,b))
# cnt = (n_list[-1]-n_list[0])//gap_list[0]
# print(cnt-l+1)

#https://www.acmicpc.net/problem/9536
# for _ in range(one()):
#     a = inputing().split()
#     while True:
#         b = inputing()
#         if b == "what does the fox say?":
#             break
#         b = b.split()
#         for i in range(len(a)):
#             if a[i] == b[-1]:
#                 a[i]=""
#     a = [i for i in a if len(i) != 0]
#     print(*a)

#https://www.acmicpc.net/problem/15489
# r,c,l = wow()
# n_list = [[1],[1,1],[1,2,1]]
# for _ in range(30):
#     new_list = []
#     for i in range(1,len(n_list[-1])):
#         new_list.append(n_list[-1][i]+n_list[-1][i-1])
#     new_list.insert(0,1)
#     new_list.append(1)
#     n_list.append(new_list)
# index = 1
# cnt = 0
# for i in range(r-1,r+l-1):
#     cnt+=sum(n_list[i][c-1:(c-1)+index])
#     # print(n_list[i][c-1:(c-1)+index])
#     index+=1
# print(cnt)    



















