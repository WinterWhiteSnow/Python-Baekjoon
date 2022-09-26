import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#7785
# n_dict = {}
# for _ in range(one()):
#     a,b = inputing().split()
#     n_dict[a]=b
# n_list = sorted([a for a,b in n_dict.items() if b == "enter"],reverse=True)
# print(*n_list,sep="\n")

#2667
# r = one()
# n_list = [list(inputing()) for _ in range(r)]
# n_dict = {}
# def bfs(x,y,cnt):
#     if 0<=x<=r-1 and 0<=y<=r-1:
#         if n_list[x][y] == "0":
#             return
#         if n_list[x][y] == "1":
#             n_list[x][y]=cnt
#             if cnt not in n_dict:
#                 n_dict[cnt]=1
#             else:
#                 n_dict[cnt]+=1
#             bfs(x+1,y,cnt)
#             bfs(x-1,y,cnt)
#             bfs(x,y+1,cnt)
#             bfs(x,y-1,cnt)
#     else:
#         return cnt+1
# cnt = 2
# for x in range(r):
#     for y in range(r):
#         bfs(x,y,cnt)
#         cnt+=1
# list_list = sorted(n_dict.values())
# print(len(list_list))
# print(*list_list,sep="\n")

# sys.setrecursionlimit(10**7)
# r,l,rr = wow()
# n_list = [[0]*l for _ in range(r)]
# for _ in range(rr):
#     x,y,xx,yy = wow()
#     for y_index in range(y,yy):
#         for x_index in range(x,xx):
#             n_list[y_index][x_index]="X"
# n_dict = {}
# def bfs(x,y,cnt):
#     if 0<=x<=l-1 and 0<=y<=r-1:
#         if n_list[y][x] != 0:
#             return
#         else:
#             n_list[y][x]=cnt
#             if cnt not in n_dict:
#                 n_dict[cnt]=1
#             else:
#                 n_dict[cnt]+=1
#             bfs(x-1,y,cnt)
#             bfs(x+1,y,cnt)
#             bfs(x,y-1,cnt)
#             bfs(x,y+1,cnt)
#     else:
#         return 
# cnt = 1        
# for y in range(r):
#     for x in range(l):
#         bfs(x,y,cnt)
#         cnt+=1

# print(len(n_dict.keys()))
# print(*sorted(n_dict.values()))

l = one()
n_list = list(wow())







