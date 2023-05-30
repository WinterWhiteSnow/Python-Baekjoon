import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())



# https://www.acmicpc.net/problem/10026
# from collections import deque
# n = one()
# n_list = [inputing() for _ in range(n)]
# nomal = [[False]*n for _ in range(n)]
# red = [[False]*n for _ in range(n)]
# red_list = deque()
# index = 1
# move = [(0,1),(0,-1),(1,0),(-1,0)]
# for y in range(n):
#     for x in range(n):
#         if nomal[y][x]== False:
#             nomal_list = deque()    
#             nomal_list.append((y,x))
#             state = n_list[y][x]
#             nomal[y][x]=index
#             # print("start!",nomal_list)
#             while nomal_list:
#                 yy,xx = nomal_list.popleft()
#                 for yyy,xxx in move:
#                     yyyy,xxxx = yyy+yy,xxx+xx
#                     if 0<=yyyy<n and 0<=xxxx<n:
#                         if nomal[yyyy][xxxx]==False:
#                             if n_list[yyyy][xxxx]==state:
#                                 nomal[yyyy][xxxx]=index
#                                 nomal_list.append((yyyy,xxxx))
#             index+=1   
# index_index = 1             
# for y in range(n):
#     for x in range(n):
#         if red[y][x]== False:
#             red_list = deque()    
#             red_list.append((y,x))
#             state = n_list[y][x]
#             red[y][x]=index_index
#             # print("start!",red_list)
#             while red_list:
#                 yy,xx = red_list.popleft()
#                 for yyy,xxx in move:
#                     yyyy,xxxx = yyy+yy,xxx+xx
#                     if 0<=yyyy<n and 0<=xxxx<n:
#                         if red[yyyy][xxxx]==False:
#                             if state == "G" or state == "R":
#                                 if n_list[yyyy][xxxx]=="G" or n_list[yyyy][xxxx]=="R":
#                                     red[yyyy][xxxx]=index_index
#                                     red_list.append((yyyy,xxxx))
#                             else:
#                                 if n_list[yyyy][xxxx]==state:
#                                     red[yyyy][xxxx]=index_index
#                                     red_list.append((yyyy,xxxx))                             
#             index_index+=1                
# # print(nomal[n-1][n-1],red[n-1][n-1])
# print(index-1,index_index-1)
# # print(*nomal,sep="\n")
# # print("?")
# # print(*red,sep="\n")

#https://www.acmicpc.net/problem/5427
# from collections import deque
# move = [(0,1),(0,-1),(1,0),(-1,0)]
# def go(fire_list,move_list):
#     cnt = 0
#     global c,r
#     while move_list:
#         temp_move = deque()
#         temp_fire = deque()
#         cnt+=1
#         # print("Start",cnt)
#         # print(*visit,sep="\n")
        
#         while fire_list:
#             y,x = fire_list.popleft()
#             for yy,xx in move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if visit[yyy][xxx] == False:
#                         visit[yyy][xxx]=True
#                         temp_fire.append((yyy,xxx))
#                     if visit[yyy][xxx]=="X":
#                         visit[yyy][xxx]=True
#                         temp_fire.append((yyy,xxx))
#         while move_list:
#             y,x = move_list.popleft()
#             for yy,xx in move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if visit[yyy][xxx] == False:
#                         if yyy==0 or yyy==r-1 or xxx==0 or xxx==c-1:
#                             return True,cnt+1
#                         visit[yyy][xxx]="X"
#                         temp_move.append((yyy,xxx))
#         if temp_move:
#             move_list = temp_move
#             fire_list = temp_fire
#     return False,0
# for _ in range(one()):
#     c,r = wow()
#     n_list = [inputing() for _ in range(r)]
#     fire_list = deque()
#     move_list = deque()
#     visit = [[False]*c for _ in range(r)]
#     escape = False
#     for y in range(r):
#         for x in range(c):
#             if n_list[y][x] == "#":
#                 visit[y][x]=True
#             if n_list[y][x] =="@":
#                 if y==0 or y==r-1 or x==0 or x==c-1:
#                     print(1)
#                     escape =True
#                     break
#                 move_list.append((y,x))
#             if n_list[y][x] == "*":
#                 fire_list.append((y,x))
#                 visit[y][x]=True
#         if escape:
#             break
#     if escape == False:
#         check,cnt = go(fire_list,move_list)
#         if check:
#             print(cnt)
#         else:
#             print("IMPOSSIBLE")

#https://www.acmicpc.net/problem/1697
# from collections import deque
# a,b = wow()
# total = [False]*100001
# move = deque()
# if a>b:
#     print(a-b)
# else:
#     a,b = min(a,b),max(a,b)
#     # print("start!!!",a,b)
#     total[a]=1
#     move.append(a)
#     # max_max = max(a,b)
#     while move:
#         state = move.popleft()
#         index = total[state]
#         if state+1 <= 100000:
#             if total[state+1]==False:
#                 total[state+1]=index+1
#                 move.append(state+1)
#             else:
#                 if total[state+1]>index+1:
#                     total[state+1]=index+1
#                     move.append(state+1)
#         if 0<=state-1 <= 100000:
#             if total[state-1]==False:
#                 total[state-1]=index+1
#                 move.append(state-1)
#             else:
#                 if total[state-1]>index+1:
#                     total[state-1]=index+1
#                     move.append(state-1)

#         if state*2 <= 100000:
#             if total[state*2]==False:
#                 total[state*2]=index+1
#                 move.append(state*2)
#             else:
#                 if total[state*2]>index+1:
#                     total[state*2]=index+1
#                     move.append(state*2)
#         # print(move)
#         # print(total)
#     print(total[b]-1)            
#     # print(total[:b+1])   

#https://www.acmicpc.net/problem/12851
# from collections import deque
# total = [False]*100001
# a,b = wow()
# n_dict = {}
# for i in range(100001):
#     n_dict[i]={}
# if a>b:
#     print(a-b)
#     print(1)
# elif a==b:
#     print(0)
#     print(1)
# else:
#     total[a]=1
#     move = deque()
#     move.append((a,""))
#     while move:
#         state,d = move.popleft()
#         index = total[state]
#         x,y,z = state+1,state-1,state*2
#         if x <= 100000:
#             if total[x]==False:
#                 total[x]=index+1
#                 dd = d+"+"
#                 n_dict[x][dd]=1
#                 move.append((x,dd))
#             elif total[x]>=index+1:
#                 total[x]=index+1
#                 dd = d+"+"
#                 n_dict[x][dd]=1
#                 move.append((x,dd))
#         if y >=0:
#             if total[y]==False:
#                 total[y]=index+1
#                 dd = d+"-"
#                 n_dict[y][dd]=1
#                 move.append((y,dd))
#             elif total[y]>=index+1:
#                 total[y]=index+1
#                 dd = d+"-"
#                 n_dict[y][dd]=1
#                 move.append((y,dd))
#         if z <= 100000:
#             if total[z]==False:
#                 total[z]=index+1
#                 dd = d+"x"
#                 n_dict[z][dd]=1
#                 move.append((z,dd))
#             elif total[z]>=index+1:
#                 total[z]=index+1
#                 dd = d+"x"
#                 n_dict[z][dd]=1
#                 move.append((z,dd))
#         # print(move)
#         # for i in range(20):
#         #     print(i,n_dict[i])
#         # exit()
#     print(total[b]-1)
#     print(len(n_dict[b]))                

#https://www.acmicpc.net/problem/13549
# from collections import deque    
# total=[0]*100001
# a,b = wow()
# if a>b:
#     print(a-b)
# else:
#     total[a]=1
#     move = deque()
#     move.append(a)
#     while move:
#         state = move.popleft()
#         index = total[state]
#         x,y,z = state+1,state-1,state*2
#         if x<=100000:
#             if total[x] == False:
#                 total[x]=index+1
#                 move.append(x)
#             elif total[x]>index+1:
#                 total[x]=index+1
#                 move.append(x)
#         if y>=0:
#             if total[y] == False:
#                 total[y]=index+1
#                 move.append(y)
#             elif total[y]>index+1:
#                 total[y]=index+1
#                 move.append(y)
#         if z<=100000:
#             if total[z] == False:
#                 total[z]=index
#                 move.append(z)
#             elif total[z]>index:
#                 total[z]=index
#                 move.append(z)
#     print(total[b]-1)

          
                












