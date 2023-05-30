import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/20056
# n,m,k = wow()
# n_list = [[0]*n for _ in range(n)]
# move = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
# index_list = []
# for _ in range(m):
#     r,c,g,s,d = wow()
#     r,c = r-1,c-1
#     index_list.append((r,c,g,s,d))
# for kk in range(k):
#     total_list = []
#     temp_list = []
#     visited = [[False]*(n) for _ in range(n)]
#     while index_list:
#         r,c,g,s,d = index_list.pop()
#         if type(g) == list:
#             g = g[0]
#         if type(s) == list:
#             s = s[0]
#         if type(d) == list:
#             d = d[0]
#         # print("start!!!",r,c,g,s,d)
#         y_d,x_d = move[d]
#         y_d*=s
#         x_d*=s
#         r+=y_d
#         r%=n
#         c+=x_d
#         c%=n
#         # print("move_end",r,c)
#         if visited[r][c] == False:
#             temp_list.append((r,c))
#             visited[r][c]=[[g],[s],[d]]
#         else:
#             visited[r][c][0]+=[g]
#             visited[r][c][1]+=[s]
#             visited[r][c][2]+=[d]
#     # print("temp",temp_list,visited)
#     while temp_list:
#         y,x = temp_list.pop()[:2]
#         g,s,d = visited[y][x]
#         # print(y,x,g,s,d)
#         if len(d)>1:
#             odd = 0
#             even = 0
#             for dd in d:
#                 if dd%2:
#                     odd+=1
#                 else:
#                     if dd%2==0:
#                         even+=1
#             if even == len(d) or odd == len(d):
#                 direction = [0,2,4,6]
#             else:
#                 direction = [1,3,5,7]
#             ss = sum(s)//len(s)
#             gg = sum(g)//5
#             if gg == 0:
#                 continue
#             for ddd in direction:
#                 total_list.append((y,x,gg,ss,ddd))
#         else:
#             total_list.append((y,x,g,s,d))
#     # print(kk)
#     # print(total_list)
#     index_list = total_list
# # print("real_end!!!",total_list)
# cnt = 0
# for a in total_list:
#     g = a[2]
#     if type(g) == list:
#         g=g[0]
#     cnt+=g
# print(cnt)


# check([3, 2, 2, 1, 1, 1])  
# check([3, 3, 2, 1, 1, 2]) 
# 1 [3, 3, 2, 1, 1, 1]
# 2 [3, 3, 2, 1, 1, 2]
# 3 [3, 3, 2, 3, 3, 3]
# 5 [1, 1, 2, 3, 3, 2]
n_list = [1,2,3,4,5]
for a in range(2,2-2,-1):
    print(n_list[a])











