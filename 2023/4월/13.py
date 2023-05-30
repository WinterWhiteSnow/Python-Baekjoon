import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/13459
#https://www.acmicpc.net/problem/15644
#https://www.acmicpc.net/problem/15653
# sys.setrecursionlimit(10**7)
# r,c =wow()
# r_y,r_x = 0,0
# b_y,b_x = 0,0
# g_y,g_x = 0,0
# visit = [[0]*c for _ in range(r)]
# n_list = [list(inputing()) for _ in range(r)]
# for y in range(r):
#     for x in range(c):
#         # print("start!",y,x,n_list[y][x])
#         if n_list[y][x] == "B":
#             b_y,b_x = y,x
#         if n_list[y][x] == "O":
#             g_y,g_x = y,x
#         if n_list[y][x] == "R":
#             r_y,r_x = y,x
#         if n_list[y][x] == "#":
#             # print("wow!!",y,x)
#             visit[y][x]=1
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# n_dict = {}
# max_max = 10000000000000000000001
# #2461
# def go(b_y,b_x,r_y,r_x,cnt):
#     global r,c,g_y,g_x,max_max
#     if cnt > max_max:
#         return
#     # print("start!!!",cnt)
#     # print("BLUE",b_y,b_x)
#     # print("RED",r_y,r_x)
#     for d in range(4):
#         check = True # 파란구슬이 안빠졌는가
#         hole = False # 빨간구슬이 빠졌는가
#         repeat = False # 이동중 한번 막혔는가
#         move_y,move_x = move[d]
#         B_y,B_x =b_y,b_x
#         R_y,R_x=r_y,r_x
#         while True:
#             by,bx = B_y+move_y,B_x+move_x
#             if 0<=by<r and 0<=bx<c:
#                 if by==R_y and bx == R_x:
#                     repeat = True
#                     break
#                 if by==g_y and bx==g_x:
#                     check = False
#                     break
#                 if visit[by][bx]==0:
#                     B_y,B_x = by,bx
#                 else:
#                     break
#             else:
#                 break
#         if check == False:
#             continue
#         while True:
#             ry,rx = R_y+move_y,R_x+move_x
#             if 0<=ry<r and 0<=rx<c:
#                 if ry==B_y and rx == B_x:
#                     break
#                 if ry==g_y and rx==g_x:
#                     hole = True
#                     R_y,R_x = -1,-1
#                     break
#                 if visit[ry][rx]==0:
#                     R_y,R_x = ry,rx
#                 else:
#                     break
#             else:
#                 break
#         if repeat == True:
#             while True:
#                 by,bx = B_y+move_y,B_x+move_x
#                 if 0<=by<r and 0<=bx<c:
#                     if by==R_y and bx == R_x:
#                         break
#                     if by==g_y and bx==g_x:
#                         check = False
#                         break
#                     if visit[by][bx]==0:
#                         B_y,B_x = by,bx
#                     else:
#                         break
#                 else:
#                     break
#         if check == hole == True:
#             if max_max > cnt+1:
#                 max_max = cnt+1
#                 continue
#         if check == False:
#             continue
#         key = f"{R_y}{R_x}"
#         value = f"{B_y}{B_x}"
#         if key not in n_dict:
#             n_dict[key]={}
#             n_dict[key][value]=cnt+1
#         else:
#             if value not in n_dict[key]:
#                 n_dict[key][value]=cnt+1
#             else:
#                 if n_dict[key][value]>cnt+1:
#                     n_dict[key][value]=cnt+1
#                 else:
#                     continue
#         go(B_y,B_x,R_y,R_x,cnt+1)
# go(b_y,b_x,r_y,r_x,0)    
# if max_max ==  10000000000000000000001:
#     print(-1)
# else:
#     print(max_max)

n_dict = {}
move = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
n_list = []
total = 0
d = 0
visit = [0]*17
for y in range(4):
    list_list = list(wow())
    new_list = []
    for x in range(0,len(list_list),2):
        if y==x==0:
            total+=list_list[x]
            d = list_list[x+1]-1
            new_list.append([0,"X"])
            visit[list_list[x]]=1
            continue
        new_list.append([list_list[x],list_list[x+1]-1])
    n_list.append(new_list)
max_max = 0
def step(number,list_list,y,x):
    for yy in range(4):
        for xx in range(4):
            # print("dfdfdf",list_list[yy][xx])
            if list_list[yy][xx][0]==number:
                y_index,x_index,direction = yy,xx,list_list[yy][xx][1]
                for _ in range(8):
                    direction%=8
                    my,mx = move[direction]
                    next_y,next_x = y_index+my,x_index+mx
                    if 0<=next_y<4 and 0<=next_x<4:
                        if next_y == y and next_x == x:
                            direction+=1
                            continue
                        list_list[y_index][x_index][1]=direction
                        list_list[y_index][x_index],list_list[next_y][next_x]=list_list[next_y][next_x],list_list[y_index][x_index]
                        return
                    else:
                        direction+=1
                        continue
    return
    
def go(y,x,d,cnt,visit,list_list):
    global max_max
    move_y,move_x = move[d]
    print("start",cnt)
    print(y,x,d,move[d])
    for i in list_list:
        print(i)
    # new_list = []
    # for i in list_list:
    #     aa = []    
    #     for a in i:
    #         aa.append(a)
    #     new_list.append(aa)
        
    for i in range(1,17):
        if visit[i] == 0:
            step(i,list_list,y,x)
    print("end",cnt)
    for i in list_list:
        print(i)
    # exit()
    while True:
        y+=move_y
        x+=move_x
        # print(y,x,"!!!!")
        if 0<=y<4 and 0<=x<4:
            new_list = []
            for i in list_list:
                aa = []    
                for a in i:
                    aa.append(a)
                new_list.append(aa)
            key = new_list[y][x][0]
            if key == 0:
                max_max = max(max_max,cnt)
                continue
            v = [i for i in visit]
            v[key]=1
            new_d = new_list[y][x][1]
            new_list[y][x]=[0,"X"]
            go(y,x,new_d,cnt+key,v,new_list)
        else:
            break
    max_max = max(max_max,cnt)
go(0,0,d,total,visit,n_list)
print(max_max)
       
                    
                    
        
    
        
        
            
    
            














