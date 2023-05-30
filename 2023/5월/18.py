import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/27964
# l = one()
# n_list = inputing().split()
# n_dict=  {}
# for n in n_list:
#     if n[-6:] == "Cheese":
#         n_dict[n]=1
# if len(n_dict) >= 4:
#     print("yummy")
# else:
#     print("sad")

#https://www.acmicpc.net/problem/27648
# r,c,k = wow()
# n_list = [[0]*c for _ in range(r)]
# total = True
# num = 1
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] == 0:
#             x_index,y_index=x,y
#             while 0<=x_index<c and 0<=y_index<r:
#                 n_list[y_index][x_index]=num
#                 y_index+=1
#                 x_index-=1
#             num+=1
#     # print(*n_list[y])
# if n_list[r-1][c-1] > k:
#     print("NO")
# else:
#     print("YES")
#     for n in n_list:
#         print(*n)


        














