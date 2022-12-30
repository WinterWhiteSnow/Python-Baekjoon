import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15905
# r =one()
# n_list = [list(wow()) for _ in range(r) ]
# if r <= 5:
#     print(0)
# else:
#     n_dict = {}
#     n_list.sort(key=lambda x: x[1])
#     n_list.sort(key=lambda x: x[0],reverse=True)
#     for i in range(4,len(n_list)):
#         a,b = n_list[i]
#         if a not in n_dict:
#             n_dict[a]=[b]
#         else:
#             n_dict[a]+=[b]
#     key = n_list[4][0]
#     print(len(n_dict[key])-1)

#https://www.acmicpc.net/problem/1730
# l = one()
# n_list = list(inputing())
# list_list = [["."]*(l) for _ in range(l)]
# y,x = 0,0
# for i in n_list:
#     x_index,y_index = x,y
#     if i == "U":
#         y_index-=1
#         symbol = "|"
#     if i == "D":
#         y_index+=1
#         symbol = "|"
#     if i == "R":
#         x_index+=1
#         symbol="-"
#     if i == "L":
#         x_index-=1
#         symbol="-"
#     if 0<=x_index<=l-1 and 0<=y_index<=l-1:
#         if 0<=x<=l-1 and 0<=y<=l-1:
#             if list_list[y][x] == ".":
#                 list_list[y][x]=symbol
#             else:
#                 if list_list[y][x] != symbol:
#                     list_list[y][x]="+"
#             # print(y_index,x_index)
#             if 0<=x_index<=l-1 and 0<=y_index<=l-1:
#                 if list_list[y_index][x_index] == ".":
#                     list_list[y_index][x_index]=symbol
#                 else:
#                     if list_list[y_index][x_index] != symbol:
#                         list_list[y_index][x_index]="+"    
#                 y,x = y_index,x_index
#     # print(i,y,x,y_index,x_index)
# for i in list_list:
#     print(*i,sep="")

#https://www.acmicpc.net/problem/24912
# l = one()
# n_list = list(wow())
# if l > 2:
#     check ="yes"
#     for i in range(l-2):
#         a,b,c = n_list[i],n_list[i+1],n_list[i+2]
#         if abs(a-c) == 2:
#             cnt = min(a,c)+1
#         else:
#             cnt = max(a,c)+1
#         if cnt >3:
#             cnt-=3
#         if b == 0:
#             n_list[i+1]=cnt
#         a,b,c = n_list[i],n_list[i+1],n_list[i+2]
#         if a==b or b==c:
#             check="no"
#     if n_list[0] == 0:
#         cnt = n_list[1]+1
#         if cnt > 3:
#             cnt-=3
#         n_list[0]=cnt
#     if n_list[-1] == 0:
#         cnt = n_list[-2]+1
#         if cnt > 3:
#             cnt-=3
#         n_list[-1]=cnt
#     if check == "yes":
#         print(*n_list)
#     else:
#         print(-1)
# elif l == 2:
#     if len(set(n_list)) != len(n_list):
#         if set(n_list) != {0}:
#             print(-1)
#             exit()
#     if n_list[0] == 0:
#         cnt = n_list[1]+1
#         if cnt > 3:
#             cnt-=3
#         n_list[0]=cnt     
#     if n_list[-1] == 0:
#         cnt = n_list[-2]+1
#         if cnt > 3:
#             cnt-=3
#         n_list[-1]=cnt
#     print(*n_list)
# else:
#     if n_list[0] == 0:
#         print(1)    
#     else:
#         print(*n_list)


    
    











