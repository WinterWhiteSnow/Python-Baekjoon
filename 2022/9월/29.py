import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#버블정렬1
# l,k = wow()
# n_list = list(wow())
# cnt = 0
# for _ in range(l-1):
#     for i in range(l-1):
#         if n_list[i]<n_list[i+1]:
#             pass
#         else:
#             cnt+=1
#             n_list[i],n_list[i+1]=n_list[i+1],n_list[i]
#             if cnt == k:
#                 print(n_list[i],n_list[i+1])
#                 exit()
# print(-1)

#버블정렬2
# l,k = wow()
# n_list = list(wow())
# cnt = 0
# for _ in range(l-1):
#     for i in range(l-1):
#         if n_list[i]<n_list[i+1]:
#             pass
#         else:
#             cnt+=1
#             n_list[i],n_list[i+1]=n_list[i+1],n_list[i]
#             if cnt == k:
#                 print(*n_list)
#                 exit()
# print(-1)

# n = one()
# x,y = 1,1
# for _ in range(n-2):
#     x,y = (x+y)%1000000007,x
#     # print(x,y)
# print(x,n-2)

#오목
# n_list = [list(wow()) for _ in range(19)]
# for y in range(19):
#     for x in range(19):
#         if n_list[y][x] != 0:
#             cnt = 0
#             if 0<=x+4<=18: # 가로
#                 if n_list[y][x:x+5] == [n_list[y][x]]*5:
#                     n_dict= {}
#                     state = []
#                     for x_index in range(19):
#                         if n_list[y][x_index]==n_list[y][x]:
#                             state.append([y,x_index])
#                         else:
#                             if len(state) not in n_dict:
#                                 n_dict[len(state)]=[state]
#                             else:
#                                 n_dict[len(state)]+=[state]
#                                 state=[]
#                     if len(state) not in n_dict:
#                         n_dict[len(state)]=[state]
#                     else:
#                         n_dict[len(state)]+=[state]
#                     if 5 in n_dict:
#                         y,x = n_dict[5][0][0]
#                         print(n_list[y][x])
#                         print(y+1,x+1)
#                         exit()
                        
#             if 0<=y+4<=18: #세로
#                 cnt = 0
#                 for index in range(y,y+5):
#                     cnt+=1 if n_list[index][x] == n_list[y][x] else 0
#                 if cnt == 5:
#                     # print("second")
#                     state = []
#                     count = 0
#                     n_dict= {}
#                     for y_index in range(19):
#                         if n_list[y_index][x] == n_list[y][x]:
#                             state.append([y_index,x])
#                         else:
#                             if len(state) not in n_dict:
#                                 n_dict[len(state)]=[state]
#                             else:
#                                 n_dict[len(state)]+=[state]
#                                 state=[]
#                     if len(state) not in n_dict:
#                         n_dict[len(state)]=[state]
#                     else:
#                         n_dict[len(state)]+=[state]
#                     if 5 in n_dict:
#                         y,x = n_dict[5][0][0]
#                         print(n_list[y][x])
#                         print(y+1,x+1)
#                         exit()

                        
#             if 0<=x+4<=18 and 0<=y+4<=18:
#                 cnt = 1
#                 for index in range(1,5):
#                     cnt+=1 if n_list[y+index][x+index] == n_list[y][x] else 0
#                 if cnt == 5:
#                     # print("third",cnt,y,x,n_list[y] y+1 x+1
#                     xx,yy = x,y
#                     while 0<xx<18 and 0<yy<18:
#                         xx-=1
#                         yy-=1
#                     state = []
#                     n_dict = {}
#                     while 0<=xx<=18 and 0<=yy<=18:
#                         if n_list[yy][xx] == n_list[y][x]:
#                             state.append([yy,xx])
#                         else:
#                             if len(state) not in n_dict:
#                                 n_dict[len(state)]=[state]
#                             else:
#                                 n_dict[len(state)]+=[state]
#                                 state=[]
#                         xx+=1
#                         yy+=1
                        
#                     if len(state) not in n_dict:
#                         n_dict[len(state)]=[state]
#                     else:
#                         n_dict[len(state)]+=[state]
#                     if 5 in n_dict:
#                         y,x = n_dict[5][0][0]
#                         print(n_list[y][x])
#                         print(y+1,x+1)
#                         exit()
                        
#             if 0<=x-4<=18 and 0<=y+4<=18:
#                 cnt = 1
#                 for index in range(1,5):
#                     cnt+=1 if n_list[y+index][x-index] == n_list[y][x] else 0
#                 if cnt == 5:
#                     # print("fourth")
#                     xx,yy = x,y
#                     while 0<xx<18 and 0<yy<18:
#                         yy-=1
#                         xx+=1
#                     count = 0
#                     state = []
#                     n_dict ={}
#                     while 0<=xx<=18 and 0<=yy<=18:
#                         if n_list[yy][xx] == n_list[y][x]:
#                             state.append([yy,xx])
#                         else:
#                             if len(state) not in n_dict:
#                                 n_dict[len(state)]=[state]
#                             else:
#                                 n_dict[len(state)]+=[state]
#                                 state=[]
#                         yy+=1
#                         xx-=1
#                     if len(state) not in n_dict:
#                         n_dict[len(state)]=[state]
#                     else:
#                         n_dict[len(state)]+=[state]
#                     if 5 in n_dict:
#                         y,x = n_dict[5][0][0]
#                         print(n_list[y][x])
#                         a,b = n_dict[5][0][-1]
#                         print(a+1,b+1)
#                         exit()      
# print(0)







