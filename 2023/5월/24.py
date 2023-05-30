import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16926
# def check(y,x):
#     global r,c
#     start_y,start_x = y,x
#     fy,fx = y,x
#     move_index = 0
#     state = False
#     while True:
#         my,mx = move[move_index]
#         yy,xx = fy+my,fx+mx
#         if state == True:
#             if fy==start_y and fx==start_x:
#                 break
        
#         if 0<=yy<r and 0<=xx<c:
#             if v[yy][xx]==0:
#                 v[yy][xx]=1
#                 new_list[yy][xx]=n_list[fy][fx]
#                 fy,fx = yy,xx
#             else:
#                 move_index+=1
#                 move_index%=4
#         else:
#             move_index+=1
#             move_index%=4
#         state= True
# r,c,k = wow()
# n_list = [list(wow()) for _ in range(r)]
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# for kk in range(k):
#     index = c
#     new_list = [[0]*c for _ in range(r)]
#     v = [[0]*c for _ in range(r)]
#     for y in range(r):
#         for x in range(c):
#             if v[y][x] == 0:
#                 check(y,x)
#     n_list = new_list
# for i in n_list:
#     print(*i)

#https://www.acmicpc.net/problem/13333
# l = one()
# n_list = sorted(list(wow()))
# total = [0]*(max(n_list)+1)
# max_max = 0
# for i in range(l):
#     score = n_list[i]
#     for num in range(1,score+1):
#         total[num]+=1
# for i in range(max(n_list)+1):
#     # print(i,total[i])
#     if i<=total[i]:
#         max_max=i
# print(max_max)


















