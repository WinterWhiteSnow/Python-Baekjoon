import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/19236
# n_dict = {}
# move = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
# n_list = []
# total = 0
# d = 0
# visit = [0]*17
# for y in range(4):
#     list_list = list(wow())
#     new_list = []
#     for x in range(0,len(list_list),2):
#         if y==x==0:
#             total+=list_list[x]
#             d = list_list[x+1]-1
#             new_list.append([0,"X"])
#             visit[list_list[x]]=1
#             continue
#         new_list.append([list_list[x],list_list[x+1]-1])
#     n_list.append(new_list)
# max_max = 0
# def step(number,list_list,y,x):
#     for yy in range(4):
#         for xx in range(4):
#             if list_list[yy][xx][0]==number:
#                 y_index,x_index,direction = yy,xx,list_list[yy][xx][1]
#                 for _ in range(8):
#                     direction%=8
#                     my,mx = move[direction]
#                     next_y,next_x = y_index+my,x_index+mx
#                     if 0<=next_y<4 and 0<=next_x<4:
#                         if next_y == y and next_x == x:
#                             direction+=1
#                             continue
#                         list_list[y_index][x_index][1]=direction
#                         list_list[y_index][x_index],list_list[next_y][next_x]=list_list[next_y][next_x],list_list[y_index][x_index]
#                         return
#                     else:
#                         direction+=1
#                         continue
#     return
    
# def go(y,x,d,cnt,visit,list_list):
#     global max_max
#     move_y,move_x = move[d]
#     for i in range(1,17):
#         if visit[i] == 0:
#             step(i,list_list,y,x)
#     while True:
#         y+=move_y
#         x+=move_x
#         if 0<=y<4 and 0<=x<4:
#             new_list = []
#             for i in list_list:
#                 aa = []    
#                 for a in i:
#                     aa.append([f for f in a])
#                 new_list.append(aa)
#             key = new_list[y][x][0]
#             if key == 0:
#                 max_max = max(max_max,cnt)
#                 continue
#             v = [i for i in visit]
#             v[key]=1
#             new_d = new_list[y][x][1]
#             new_list[y][x]=[0,"X"]
#             go(y,x,new_d,cnt+key,v,new_list)
#         else:
#             break
#     max_max = max(max_max,cnt)
# go(0,0,d,total,visit,n_list)
# print(max_max)


# for d in range(int(input())):
#     list_list =list(map(int,input().split()))
#     total = 0
#     for i in list_list:
#         if i%2:
#             total+=i
#     print("#"+str(d+1),total)
























