import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/13460
# r,c = wow()
# total = 0
# r_y,r_x = 0,0
# b_y,b_x = 0,0
# g_y,g_x = 0,0
# visit = [[0]*c for _ in range(r)]
# n_list = []
# for y in range(r):
#     list_list = list(inputing())
#     for x in range(c):
#         if list_list[x]=="#":
#             visit[y][x]=1
#         if list_list[x]=="O":
#             g_y,g_x = y,x
#             visit[y][x]=1
#         if list_list[x]=="R":
#             r_y,r_x = y,x
#         if list_list[x]=="B":
#             b_y,b_x = y,x
#     n_list.append(list_list)
# time = 100000000000000000000000000001
# move = [(0,1),(0,-1),(1,0),(-1,0)]
# n_dict = {}
# def go(yy,xx,y,x,cnt,before_move):
#     global r,c,b_y,b_x,g_y,g_x,time
#     if cnt+1 > 10:
#         return
#     for d in range(4):
#         plus_y,plus_x = move[d]
#         B_y,B_x = yy,xx
#         R_y,R_x = y,x
#         repeat = False
#         check = True
#         hole = False
#         while True:
#             by,bx = B_y+plus_y,B_x+plus_x
#             if 0<=by<r and 0<=bx<c:
#                 if by==R_y and bx==R_x:
#                     repeat = True
#                     break
#                 if visit[by][bx] == 0:
#                     B_y,B_x = by,bx
#                 elif visit[by][bx] == 1:
#                     if by == g_y and bx == g_x:
#                         check = False
#                         break
#                     else:
#                         break
#                 else:
#                     break
#             else:
#                 break
#         if check ==  False:
#             continue
#         while True:
#             ry,rx = R_y+plus_y,R_x+plus_x
#             if 0<=ry<r and 0<=rx<c:
#                 if visit[ry][rx] == 0:
#                     if ry == B_y and rx == B_x:
#                         break
#                     else:
#                         R_y,R_x = ry,rx
#                 elif visit[ry][rx] == 1:
#                     if ry == g_y and rx == g_x:
#                         R_y,R_x = -1,-1
#                         hole = True
#                         break
#                     else:
#                         break
#                 else:
#                     break
#             else:
#                 break
#         if repeat == True:
#             while True:
#                 by,bx = B_y+plus_y,B_x+plus_x
#                 if 0<=by<r and 0<=bx<c:
#                     if by==R_y and bx==R_x:
#                         break
#                     if visit[by][bx] == 0:
#                         B_y,B_x = by,bx
#                     elif visit[by][bx] == 1:
#                         if by == g_y and bx == g_x:
#                             check = False
#                             break
#                         else:
#                             break
#                     else:
#                         break
#                 else:
#                     break
#         if check == False:
#             continue
#         if check == hole == True:
#             if time > cnt+1:
#                 time = cnt+1
#             continue
#         if B_y == yy and B_x == xx and R_y == y and R_x == x:
#             continue
#         key = f"{R_y}{R_x}"
#         if key not in n_dict:
#             n_dict[key]={f"{B_y}{B_x}":cnt+1}
#         else:
#             if f"{B_y}{B_x}" not in n_dict[key]:
#                 n_dict[key][f"{B_y}{B_x}"]=cnt+1
#             else:
#                 if n_dict[key][f"{B_y}{B_x}"] > cnt+1:
#                     n_dict[key][f"{B_y}{B_x}"] = cnt+1
#                 else:
#                     continue
#         go(B_y,B_x,R_y,R_x,cnt+1,d)

# go(b_y,b_x,r_y,r_x,0,5)
# print(time if time != 100000000000000000000000000001 else -1)

n_dict= {}
n_dict["wow"]={}
n_dict["wow"]["yes"]=1
print(n_dict)
        















