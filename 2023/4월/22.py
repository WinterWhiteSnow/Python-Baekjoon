# import sys

# inputing = lambda : sys.stdin.readline().rstrip()
# wow = lambda : map(int,inputing().split())
# one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1915
# r,c =wow()
# n_list = []
# for _ in range(r):
#     list_list = list(map(int,list(inputing())))
#     n_list.append(list_list)
# v = [[0]*(c+1) for _ in range(r+1)]
# # print(v)
# max_max = 0
# for y in range(1,r+1):
#     for x in range(1,c+1):
#         y_index,x_index = y-1,x-1
#         if n_list[y-1][x-1] == 1:
#             v[y][x]=min(v[y-1][x],v[y][x-1],v[y-1][x-1])+1
#         max_max = max(max_max,v[y][x])
# print(max_max*max_max)

# for t in range(int(input())):
#     t = t+1
#     n,m = map(int,input().split())
#     print("#"+str(t),end=" ")
#     str_str = int("1"*n,2)
#     s = bin(m)[2:]
#     if int(s[-n:],2) == str_str:
#         print("ON")
#     else:
#         print("OFF")

# import string
# str_str = list(string.ascii_lowercase)
# n_dict = {}
# for i in range(26):
#     n_dict[str_str[i]]=i
# for t in range(int(input())):
#     t = t+1
#     cnt = 0
#     n_list = list(input())
#     for i in range(len(n_list)):
#         if n_dict[n_list[i]] == i:
#             cnt+=1
#         else:
#             break
#     print("#"+str(t),cnt)

# for t in range(int(input())):
#     t = t+1
#     total,a,b,c = map(int,input().split())
#     answer = c*(total/(a+b))
#     print("#"+str(t)+f" {answer:.6f}")











