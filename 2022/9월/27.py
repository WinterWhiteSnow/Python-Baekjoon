import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# sys.setrecursionlimit(10**7)
# r,l = wow()
# n_list = [inputing().split() for _ in range(r)]
# n_dict = {}
# def bfs(x,y,cnt):
#     if 0<=x<=l-1 and 0<=y<=r-1:
#         # for i in n_list:
#         #     print(i)
#         if n_list[y][x] == "1":
#             n_list[y][x]=cnt
#             if cnt not in n_dict:
#                 n_dict[cnt]=1
#             else:
#                 n_dict[cnt]+=1
#             bfs(x-1,y,cnt)
#             bfs(x,y-1,cnt)
#             bfs(x+1,y,cnt)
#             bfs(x,y+1,cnt)
#         else:
#             return
#     else:
#         return
# cnt = 1
# for y in range(r):
#     for x in range(l):
#         bfs(x,y,cnt)
#         cnt+=1
# if len(n_dict) == 0:
#     print(0)
#     print(0)
# else:
#     print(len(n_dict.keys()))
#     print(max(n_dict.values()))















