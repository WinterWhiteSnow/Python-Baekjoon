import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())
     
#https://www.acmicpc.net/problem/9663
# n = one()
# visit = [0]*n
# cnt = 0
# def check(x):
#     for i in range(x):
#         if visit[i]==visit[x] or abs(x-i)==abs(visit[x]-visit[i]):
#             return False
#     return True
# def go(x):
#     global cnt
#     if x == n:
#         cnt+=1
#         return
#     for i in range(n):
#         visit[x]=i
#         if check(x):
#             go(x+1)     
# go(0)
# print(cnt)    

#https://www.acmicpc.net/problem/4179
# from collections import deque
# r,c = wow()
# n_list = [inputing() for _ in range(r)]
# fire_list = deque()
# start_y,start_x = 0,0
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# move_list = deque()
# visit = [[False]*c for _ in range(r)]
# for y in range(r):
#     for x in range(c):
#         if n_list[y][x] != ".":    
#             if n_list[y][x] == "J":
#                 start_y,start_x = y,x
#                 move_list.append((y,x))
#             if n_list[y][x] == "F":
#                 visit[y][x]=True
#                 fire_list.append((y,x))
#             if n_list[y][x] == "#":
#                 visit[y][x]=True
# cnt = 0
# escape = False
# while move_list:
#     temp_move = deque()
#     temp_index = deque()
#     cnt+=1
#     # print("start!!!",cnt)
#     # print(*visit,sep="\n")
#     while fire_list:
#         y,x = fire_list.popleft()
#         for i in range(4):
#             yyy,xxx= move[i][0]+y,move[i][1]+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if visit[yyy][xxx]==False or visit[yyy][xxx] == "X":
#                     temp_index.append((yyy,xxx))
#                     visit[yyy][xxx]=True
#     while move_list:
#         y,x = move_list.popleft()
#         for i in range(4):
#             yyy,xxx= move[i][0]+y,move[i][1]+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if visit[yyy][xxx]==False:
#                     # if yyy == 0 or yyy == r-1 or xxx ==0 or xxx == c-1:
#                     #     print(cnt+1)
#                     #     exit()
#                     temp_move.append((yyy,xxx))
#                     visit[yyy][xxx]="X"
#             else:
#                 print(cnt)
#                 exit()
#     if temp_move:
#         fire_list = temp_index
#         move_list = temp_move
# print("IMPOSSIBLE")          

            
        
                
                
    
 
            
        

            











