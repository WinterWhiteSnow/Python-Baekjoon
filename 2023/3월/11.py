import sys
from collections import deque

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/7562
# from collections import deque
# move = [(-2,1),(-1,2),(-2,-1),(-1,-2)]
# for i in range(len(move)):
#     y,x = move[i]
#     move.append((-y,x))
# for _ in range(one()):
#     r = one()
#     y,x = wow()
#     yy,xx = wow()
#     n_list = [[0]*r for _ in range(r)]
#     q = deque()
#     q.append((y,x))
#     n_list[y][x]=1
#     while q:
#         yyy,xxx = q.popleft()
#         index = n_list[yyy][xxx]
#         for yyyy,xxxx in move:
#             y_index,x_index = yyyy+yyy,xxxx+xxx
#             if 0<=y_index<r and 0<=x_index<r:
#                 if n_list[y_index][x_index] == False:
#                     n_list[y_index][x_index]=index+1
#                     q.append((y_index,x_index))
#     print(n_list[yy][xx]-1)

#https://www.acmicpc.net/problem/6593
# from collections import deque
# move = [(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
# while True:
#     l,r,c = wow()
#     if l==r==c==False:
#         break
#     n_list = deque()
#     t,y,x = 0,0,0
#     e_t,e_y,e_x = 0,0,0
#     for ll in range(l):
#         temp_list = []
#         for y_index in range(r+1):
#             list_list = list(inputing())
#             if "S" in list_list:
#                 t,y,x = ll,y_index,list_list.index("S")
#             if "E" in list_list:
#                 e_t,e_y,e_x = ll,y_index,list_list.index("E")
#             temp_list.append(list_list)
#         temp_list=temp_list[:-1]
#         n_list.append(temp_list)
#     q = deque()
#     q.append((t,y,x))
#     n_list[t][y][x]=0
#     while q:
#         tt,yy,xx = q.popleft()
#         index = n_list[tt][yy][xx]
#         for ttt,yyy,xxx in move:
#             tttt,yyyy,xxxx = tt+ttt,yy+yyy,xx+xxx
#             if 0<=tttt<l and 0<=yyyy<r and 0<=xxxx<c:
#                 if n_list[tttt][yyyy][xxxx]==".":
#                     n_list[tttt][yyyy][xxxx] = index+1
#                     q.append((tttt,yyyy,xxxx))
#                 if n_list[tttt][yyyy][xxxx]=="E":
#                     n_list[tttt][yyyy][xxxx]=index+1
                
#     answer = n_list[e_t][e_y][e_x]
#     if answer == "E":
#         print("Trapped!")
#     else:
#         print(f"Escaped in {answer} minute(s).")
#     # print(t,y,x)
#     # print(e_y,e_y,e_x)
#     # print(n_list)
    











