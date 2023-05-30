import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14503
# r,l = wow()
# y,x,d = wow()
# if d ==1:
#     d =3
# elif d == 3:
#     d = 1
# back_move = [(1,0),(0,1),(-1,0),(0,-1)]
# front_move = [(-1,0),(0,-1),(1,0),(0,1)]
# n_list = [list(wow()) for _ in range(r)]
# move_move = []

# def check(y,x):
#     global r,l,d
#     index_list = []
#     # print("now",d)
#     d_index = (d+1)%4
#     move = front_move[d_index:]+front_move[:d_index]
#     # print("move!!!!",move)
#     for ind in range(4):
#     # for yy,xx in move:
#         yy,xx = move[ind]
#         yyy,xxx = y+yy,x+xx
#         if 0<=yyy<r and 0<=xxx<l:
#             if n_list[yyy][xxx]==0:
#                 index_list.append((yyy,xxx))
#                 break
#     # print(y,x,index_list)
#     index = front_move.index((yy,xx))
#     if len(index_list)>0:
#         return index_list[0][0],index_list[0][1],index
#     else:
#         return False
# cnt = 0
# while True:
#     if n_list[y][x] == 0:
#         cnt+=1
#         n_list[y][x] = "x"
#     else:
#         a = check(y,x)
#         if a == False:
#             yy,xx = back_move[d]
#             # print(a,yy,xx,d,back_move)
#             if 0<=y+yy<r and 0<=x+xx<l:
#                 y,x = y+yy,x+xx
#                 if n_list[y][x] != 1:
#                     pass
#                 else:
#                     break
#             else:
#                 break
#         else:
#             # print("zero,else",a)
#             yyy,xxx,d = a
#             y,x = yyy,xxx
#     # if 10<=cnt <= 20:
#     #     print(y,x,d,cnt)
#     #     for i in n_list:
#     #         print(*i)

# print(cnt)            













