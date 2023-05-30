import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1788
# n = one()
# if n <0:
#     state = -1
# else:
#     state = 1
# if n == 0:
#     print(0)
#     print(0)
# else:
#     x,y = 0,1
#     for _ in range(abs(n)-1):
#         x,y = y,x+y
#         x%=1000000000
#         y%=1000000000
#     if state == -1:
#         if abs(n)%2 == 0:
#             print(-1)
#             print(y)
#         else:
#             print(1)
#             print(y)
#     else:
#         print(state)
#         print(y)

#https://www.acmicpc.net/problem/17484
# sys.setrecursionlimit(10**7)
# r,c = wow()
# n_list = [list(wow()) for _ in range(r)]
# move=  [(1,-1),(1,0),(1,1)]
# min_min = 100000000000000000000001
# def dfs(y,x,count,state):
#     global r,c,min_min
#     if y==r:
#         if min_min > count:
#             min_min = count
#     if 0<=y<r and 0<=x<c:
#         count+=n_list[y][x]
#         for d in range(3):
#             if state == d:
#                 continue
#             m = move[d]
#             a,b = m
#             dfs(y+a,x+b,count,d)
# for x in range(c):  
#     dfs(0,x,0,"none")
# print(min_min)

#https://www.acmicpc.net/problem/13270
# n_dict = {}
# n_dict[2]=1
# x,y = 2,1
# n = one()
# while True:
#     x,y = x+y,x
#     if x <= n:
#         n_dict[x]=y
#     else:
#         break
# min_min = [1000000000000001]*(n+1)
# max_max = [0]*(n+1)
# n_list = n_dict.keys()
# for key in n_list:
#     min_min[key]=n_dict[key]
#     max_max[key]=n_dict[key]
# for num in n_list:
#     for i in range(num,n+1):
#         if min_min[i-num] != 1000000000000001:
#             min_min[i]=min(min_min[i],min_min[i-num]+n_dict[num])         
#         max_max[i]=max(max_max[i],max_max[i-num]+n_dict[num])
# print(min_min[-1],max_max[-1])

#https://www.acmicpc.net/problem/16493
# day,chapter = wow()
# n_list  =  [list(wow()) for _ in range(chapter)]
# visit = [0]*chapter
# max_max = 0
# temp_list = [0]*(day+1)
# def dfs(y,days,v,cnt):
#     global day,chapter,max_max
#     d,page = n_list[y]
#     if d+days <= day:
#         cnt+=page
#         days+=d
#         if max_max < cnt:
#             max_max = cnt
#         if temp_list[days] == 0:
#             temp_list[days] = cnt
#         else:
#             if temp_list[days] <cnt:
#                 temp_list[days] = cnt
#             else:
#                 return
#         v[y]=1
#         for i in range(chapter):
#             if v[i]==1:
#                 continue
#             dfs(i,days,v,cnt)
#         v[y]=0
# for y in range(chapter):
#     dfs(y,0,visit,0)
# print(max_max)

#https://www.acmicpc.net/problem/19621
# sys.setrecursionlimit(10**7)
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# visit = [0]*r
# max_max = 0
# temp_list = [0]*r
# def dfs(time,index,visit,total):
#     global r,max_max
#     start,end,count = n_list[index]
#     if start >= time:
#         visit[index]=1
#         if index-1 >= 0:
#             visit[index-1]=1
#         if index+1 < r:
#             visit[index+1]=1
#         time = end
#         total+=count
#         if max_max < total:
#             max_max = total
#         if temp_list[index] == 0:
#             temp_list[index]=total
#         else:
#             if temp_list[index] < total:
#                 temp_list[index] = total
#             else:
#                 return
#         if index+2 < r:
#             for i in range(index+2,r):
#                 if visit[i] == 1:
#                     continue
#                 dfs(time,i,visit,total)
#         visit[index]=0
#         if index-1 >= 0:
#             visit[index-1]=0
#         if index+1 < r:
#             visit[index+1]=0
# dfs(0,0,visit,0)
# print(max_max)

#https://www.acmicpc.net/problem/19622
# r =one()
# n_list = [list(wow()) for _ in range(r)]
# v = [0]*r
# if r == 1:
#     print(n_list[0][2])
# else:
#     v[0]=n_list[0][2]
#     v[1]=max(n_list[0][2],n_list[1][2])
#     for i in range(2,r):
#         v[i]=max(v[i-1],v[i-2]+n_list[i][2])
#     print(v[-1])
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# v = [[0,0] for _ in range(r)]
# if r == 1:
#     print(n_list[0][2])
# else:
#     v[0][1]= n_list[0][2]
#     v[1][0]=max(v[0][0],v[0][1])
#     v[1][1]=v[0][0]+n_list[1][2]
#     for i in range(2,r):
#         v[i][0]=max(v[i-1][0],v[i-1][1])
#         v[i][1]=v[i-1][0]+n_list[i][2]
#     print(max(v[-1]))

#https://www.acmicpc.net/problem/9465
# for _ in range(one()):
#     l = one()
#     n_list = [list(wow()) for _ in range(2)]
#     total = [[[0,0] for _ in range(l)] for _ in range(2)]
#     total[0][0][0]=0
#     total[0][0][1]=n_list[0][0]
#     total[1][0][0]=0
#     total[1][0][1]=n_list[1][0]
#     for x in range(1,l):
#         for y in range(2): 
#             total[y][x][0]+=max(total[y][x-1][1],total[y][x-1][0],total[(y+1)%2][x-1][1],total[(y+1)%2][x-1][0])
#             total[y][x][1]=n_list[y][x]+max(total[(y+1)%2][x-1][0],total[(y+1)%2][x-1][1])
#     print(max(max(total[0][l-1]),max(total[1][l-1])))




    









