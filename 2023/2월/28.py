import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/20057
# n = one()
# n_list = [list(wow()) for _ in range(n)]
# west = [(0,-2,0.05),(-1,-1,0.1),(-1,0,0.07),(-2,0,0.02),(-1,1,0.01)]
# for i in range(1,len(west)):
#     y,x,r = west[i]
#     west.append((-y,x,r))
# west.append((0,-1))
# east = []
# for i in west:
#     if len(i)==3:
#         y,x,rate = i
#         east.append((y,-x,rate))
#     else:
#         y,x = i
#         east.append((y,-x))
# south = [(2,0,0.05),(-1,1,0.01),(0,1,0.07),(0,2,0.02),(1,1,0.1)]
# for i in range(1,len(south)):
#     y,x,rate = south[i]
#     south.append((y,-x,rate))
# south.append((1,0))
# nouth = []
# for i in south:
#     if len(i)==3:
#         y,x,rate = i
#         nouth.append((-y,x,rate))
#     else:
#         y,x = i
#         nouth.append((-y,x))

# tornado = [[False]*n for _ in range(n)]
# move = [(0,1),(1,0),(0,-1),(-1,0)]
# y,x = 0,0
# now = "west"
# tornado[0][0]=move[2]
# move_index = 0
# paint_index = (move_index+2)%4
# cnt = 0
# while True:
#     yy,xx = move[move_index]
#     yyy,xxx = y+yy,x+xx
#     if 0<=yyy<n and 0<=xxx<n:
#         if tornado[yyy][xxx]==False:
#             tornado[yyy][xxx]=move[paint_index]
#             y,x = yyy,xxx
#         else:
#             move_index+=1
#             move_index%=4
#             paint_index+=1
#             paint_index%=4
#             yy,xx = move[move_index]
#             yyy,xxx = y+yy,x+xx
#             if tornado[yyy][xxx]!=False:
#                 break
#     else:
#         move_index+=1
#         move_index%=4
#         paint_index+=1
#         paint_index%=4

# def blow(y,x,wind_wind,ex):
#     global cnt,n
#     total = n_list[y][x]
#     n_list[y][x]=0
#     ex_y,ex_x = ex
#     minus = 0
#     for i in wind_wind[:-1]:
#         yy,xx,r = i
#         y_index,x_index= yy+y,xx+x
#         index = int(total*r)
#         if 0<=y_index<n and 0<=x_index<n:
#             n_list[y_index][x_index]+=index
#         else:
#             cnt+=index
#         minus+=index    
#     total-=minus
#     final_y,final_x = wind_wind[-1]
#     yy,xx = final_y+y,final_x+x
#     if 0<=yy<n and 0<=xx<n:
#         n_list[yy][xx]+=total
#     else:
#         cnt+=total
        
        
    
# def go(y,x):
#     move_y,move_x = tornado[y][x]
#     if tornado[y][x]==(0,-1):
#         d = west
#     elif tornado[y][x]==(1,0):
#         d = south
#     elif tornado[y][x]==(0,1):
#         d=east
#     elif tornado[y][x]==(-1,0):
#         d=nouth
#     if n_list[yy][xx] != 0:
#         blow(yy,xx,d,tornado[y][x])
#     return yy,xx
# while True:
#     y,x = go(y,x)
#     if y == 0 and x == -1:
#         break
# print(cnt)





    












