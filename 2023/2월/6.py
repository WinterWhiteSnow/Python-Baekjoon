import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/21608
# r = one()
# n_list = [[0]*r for _ in range(r)]
# list_list = [list(wow()) for _ in range(r**2)]
# visited = [[False]*r  for _ in range(r)]
# cnt = 0
# index = 0
# n_dict = {}
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# while index != r**2:
#     k = list_list[index][0]
#     like_list = list_list[index][1:]
#     n_dict[k]=like_list
#     # print(k,like_list)
#     if cnt == 0:
#         n_list[1][1]=k
#         visited[1][1]=True
#     else:
#         check_list = "none"
#         for y in range(r):
#             for x in range(r):
#                 if visited[y][x]==False:
#                     like = 0
#                     zero = 0
#                     for m in move:
#                         yy,xx = y+m[0],x+m[1]
#                         if 0<=yy<=r-1 and 0<=xx<=r-1:
#                             if n_list[yy][xx] == 0:
#                                 zero+=1
#                             else:
#                                 if n_list[yy][xx] in like_list:
#                                     like+=1
#                     # print("y,x",y,x,"like,zero",like,zero)
#                     if check_list == "none":
#                         check_list = (like,zero,y,x)
#                     else:
#                         if check_list[0] < like :  
#                             check_list = (like,zero,y,x)
#                         elif check_list[0] == like and check_list[1] < zero:
#                             check_list = (like,zero,y,x)
#                         elif check_list[0] == like and check_list[1] == zero and check_list[2]>y:
#                             check_list = (like,zero,y,x)
#                         elif check_list[0] == like and check_list[1] == zero and check_list[2]==y and check_list[3] > x:
#                             check_list = (like,zero,y,x)
#                     # print("end?",check_list)
#         n_list[check_list[2]][check_list[3]]=k  
#         visited[check_list[2]][check_list[3]]=True
#         # print("state")
#         # for i in n_list:
#         #     print(*i)      
#     cnt+=1
#     index+=1
# cnt = 0
# score = {}
# score[0]=0
# score[1]=1
# score[2]=10
# score[3]=100
# score[4]=1000
# for y in range(r):
#     for x in range(r):
#         k = n_list[y][x]
#         count = 0
#         for m in move:
#             yy,xx = y+m[0],x+m[1]
#             if 0<=yy<=r-1 and 0<=xx<=r-1:
#                 if n_list[yy][xx] in n_dict[k]:
#                     count+=1
#         cnt+=score[count]
# print(cnt) 

#https://www.acmicpc.net/problem/21610
# n,m = wow()
# n_list = [list(wow()) for _ in range(n)]
# move = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
# index_list = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]
# check_list = [(-1,-1),(1,1),(1,-1),(-1,1)]
# visited = [[False]*n for _ in range(n)]
# # for y,x in index_list:
# #     visited[y][x]=True
# for _ in range(m):
#     d,step=wow()
#     index = move[d-1]
#     yy,xx = index[0]*step,index[1]*step
#     temp_list = []
#     for i in index_list:
#         y,x = yy+i[0],xx+i[1]
#         y%=n
#         x%=n
#         n_list[y][x]+=1
#         visited[y][x]=True
#         temp_list.append((y,x))
    
#     for y,x in temp_list:
#         for check in check_list:
#             yy,xx = y+check[0],x+check[1]
#             if 0<=yy<=n-1 and 0<=xx<=n-1:
#                 if n_list[yy][xx] > 0:
#                     n_list[y][x]+=1
#     t_list = []
#     for y in range(n):
#         for x in range(n):
#             if n_list[y][x] >= 2 and visited[y][x] == False:
#                 t_list.append((y,x))
#                 n_list[y][x]-=2
#     for y,x in temp_list:
#         visited[y][x]=False
#     index_list = t_list
# cnt = 0
# for y in range(n):
#     for x in range(n):
#         cnt+=n_list[y][x]
# print(cnt)















