import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/23288
# from collections import deque
# r,c,k = wow()
# n_list = [list(wow()) for _ in range(r)]
# dice = [[0]*3 for _ in range(4)]
# dice[1]=[4,1,3]
# dice[0][1]=2
# dice[2][1]=5
# dice[3][1]=6
# move = [(0,1),(1,0),(0,-1),(-1,0)]
# move_index = 0
# y,x = 0,0
# score = 0
# def dice_dice(move_index):
#     top = dice[1]#list
#     down = dice[3][1]#number
#     rotate = []
#     if move_index == 0:
#         top,down = [down]+top[:2],top[-1]
#         dice[1]=top
#         dice[3][1]=down
#     elif move_index == 1:
#         for i in range(4):
#             rotate.append(dice[i][1])
#         rotate = [rotate[-1]]+rotate[:3]
#         for i in range(4):
#             dice[i][1]=rotate[i]
#     elif move_index == 2:
#         top,down = top[1:]+[down],top[0]
#         dice[1]=top
#         dice[3][1]=down
#     else:
#         for i in range(4):
#             rotate.append(dice[i][1])
#         rotate = rotate[1:]+[rotate[0]]
#         for i in range(4):
#             dice[i][1]=rotate[i]  
# def move_dice(y,x,move_index):
#     global r,c
#     yy,xx = move[move_index]
#     yyy,xxx= y+yy,x+xx
#     if 0<=yyy<r and 0<=xxx<c:
#         pass
#     else:
#         move_index+=2
#         move_index%=4
#         yy,xx = move[move_index]
#         yyy,xxx= y+yy,x+xx
#     return yyy,xxx,move_index
# check = [(1,0),(-1,0),(0,1),(0,-1)]        
# for kk in range(k):
#     y,x,move_index = move_dice(y,x,move_index)
#     dice_dice(move_index)
#     # print("Start!!!",y,x,move_index,kk+1)
#     total = n_list[y][x]
#     index=n_list[y][x]
#     q = deque()
#     q.append((y,x))
#     count = 0
#     visit = [[False]*c for _ in range(r)]
#     while q:
#         yy,xx = q.popleft()
#         if visit[yy][xx]==False:
#             count+=1
#             visit[yy][xx]=True
#         else:
#             continue
#         # print("yy,xx",yy,xx)
#         for i in check:
#             yyy,xxx = i
#             yyyy,xxxx =yyy+yy,xxx+xx
#             if 0<=yyyy<r and 0<=xxxx<c:
#                 if visit[yyyy][xxxx]==False:
#                     if n_list[yyyy][xxxx]==index:
#                         total+=n_list[yyyy][xxxx]
#                         # visit[yyyy][xxxx]=True
#                         q.append((yyyy,xxxx))
#     score+=count*index
#     # print(kk+1,count*index,count)
#     # print(*visit,sep="\n")
#     final = dice[3][1]   
#     if final > index:
#         move_index+=1
#     elif final < index:
#         move_index-=1
#     move_index%=4
# print(score)


        
        
        
    
    















