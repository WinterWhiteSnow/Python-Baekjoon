import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/7569
# l,r,h = wow()
# n_list = []
# for _ in range(h):
#     n_list.append([list(wow()) for _ in range(r)])
# one_list = []
# one_cnt = 0
# minus_cnt = 0
# zero_cnt = 0
# for h_index in range(h):
#     for y in range(r):
#         for x in range(l):
#             c = n_list[h_index][y][x]
#             if c == 1:
#                 one_list.append([h_index,y,x])
#                 one_cnt+=1
#             elif c==-1:
#                 minus_cnt+=1
#             else:
#                 zero_cnt+=1
# if zero_cnt == 0:
#     print(0)
# else:            
#     visited = [[[False]*l for _ in range(r)] for _ in range(h)]
#     cnt = 0
#     while one_list:
#         tem_list = []
#         while one_list:
#             start = one_list.pop()
#             # print("Start",start)
#             hh,yy,xx = start
#             if visited[hh][yy][xx]==False:
#                 visited[hh][yy][xx]=True
#                 move = [[-1,0,0],[1,0,0],[0,0,-1],[0,0,1],[0,1,0],[0,-1,0]]
#                 for i in move:
#                     a,b,c = i
#                     hhh,yyy,xxx = hh+a,yy+b,c+xx
#                     if 0<=hhh<=h-1 and 0<=yyy<=r-1 and 0<=xxx<=l-1:
#                         if n_list[hhh][yyy][xxx]==0:
#                             tem_list.append([hhh,yyy,xxx])
#                             n_list[hhh][yyy][xxx]=1
#         # print(cnt)
#         # print(tem_list)
#         if tem_list:
#             one_list=tem_list
#             cnt+=1
#     for h_index in range(h):
#         for y in range(r):
#             for x in range(l):
#                 c = n_list[h_index][y][x]
#                 if c==0:
#                     print(-1)
#                     exit()
#     print(cnt)

#https://www.acmicpc.net/problem/5014
#50 1 11 4 13
# import math
# total,now,goal,up,down = wow()
# visited = [False]*(total+1)
# cnt = 0
# visited[now]=True
# check = "yes"
# while now != goal:
#     if now <goal:
#         if now+up <= total:
#             now+=up
#         else:
#             if now-down >0:
#                 now-=down
#             else:
#                 if now+up <= total:
#                     now+=up
#                 else:
#                     print("use the stairs")
#                     exit()
#     else:
#         # print("what")
#         if now-down > 0:
#             now-=down
#         else:
#             # print(now,"wowowwow")
#             if now+up <= total:
#                 now+=up
#             else:
#                 print("use the stairs")
#                 exit()
#     if now !=0:
#         if visited[now] == False:
#             visited[now]=True
#         else:
#             print("use the stairs")
#             exit()
#     else:
#         print("use the stairs")
#         exit()
#     cnt+=1
#     # print(now,cnt)
# print(cnt)

r,l =wow()
n_list = [list(wow()) for _ in range(one())]

def go(list_list,cnt):
    global r
    global l
    if cnt != 3:
        yy,xx = list_list[-1]
        for y in range(yy,r):
            
for y in range(r):
    for x in range(l):
        if n_list[y][x]==0:
            go([y,x],1)



    

            
                













