import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17144
# move1 = [(0,1),(-1,0),(0,-1),(1,0)]
# move2 = [(0,1),(1,0),(0,-1),(-1,0)]
# move_list = [move1,move2]

# from collections import deque
# r,l,t = wow()
# n_list = [list(wow()) for _ in range(r)]
# start_list = []
# for y in range(r):
#     for x in range(l):
#         if n_list[y][x] == -1:
#             start_list.append((y,x))
# start_index = 0
# move = [(0,1),(0,-1),(-1,0),(1,0)]
# def check(y,x):
#     global r,l
#     a = []
#     for yy,xx in move:
#         yyy,xxx = y+yy,x+xx
#         if 0<=yyy<=r-1 and 0<=xxx<l:
#             if n_list[yyy][xxx] != -1:
#                 a.append((yyy,xxx))
#     return a

# visited = [[False]*l for _ in range(r)]
# index_index = 0
# for y,x in start_list:
#     visited[y][x]=True    

# for count in range(t):
#     temp = []
#     for ii in n_list:
#         tt = []
#         for a in ii:
#             tt.append(a)
#         temp.append(tt)
#     for y in range(r):
#         for x in range(l):
#             if visited[y][x] == False:
#                 index_list = check(y,x)
#                 # print(y,x,index_list)
#                 spread = n_list[y][x]//5
#                 for yy,xx in index_list:
#                     temp[yy][xx]+=spread
#                 temp[y][x]-=spread*len(index_list)
#     # print("확산!!")
#     # for i in temp:
#     #     print(*i)
#     for move in move_list:
#         list_list = []
#         index_list = []
#         # print("newenw",move)
#         move_index = 0
#         start_y,start_x = start_list[start_index]
#         start_x+=1
#         q = deque()
#         q.append((start_y,start_x))
#         c = "yes"
#         list_list.append(0)
#         index_list.append((start_y,start_x))
#         while q:
#             if c == "no":
#                 break
#             yy,xx = q.popleft()
#             next_y,next_x = yy+move[move_index][0],xx+move[move_index][1]
#             # print("now",yy,xx)
#             # print("next",next_y,next_x)
#             if 0<=next_y<r and 0<=next_x<l:
#                 if visited[next_y][next_x] == False:
#                     list_list.append(temp[yy][xx])
#                     index_list.append((next_y,next_x))
#                     q.append((next_y,next_x))
#                 else:
#                     q=deque()
#                     c = "no"
#                     break
#             else:
#                 move_index+=1
#                 next_y,next_x = yy+move[move_index][0],xx+move[move_index][1]
#                 index_list.append((next_y,next_x))
#                 list_list.append(temp[yy][xx])
#                 q.append((next_y,next_x))
#             if c == "no":
#                 break
#         # print(index_list,len(index_list))
#         # print(list_list,len(list_list))
#         index=0
#         for y,x in index_list:
#             temp[y][x]=list_list[index]
#             index+=1
#         start_index+=1
#         start_index%=2
#     # for i in temp:
#     #     print(*i)
            
#     # print(count)
#     # for i in temp:
#     #     print(*i)
#     n_list=temp
# cnt = 0
# # for i in n_list:
# #     print(*i)
# for y in range(r):
#     for x in range(l):
#         if n_list[y][x] != -1:
#             cnt+=n_list[y][x]
# print(cnt)


                    
            















