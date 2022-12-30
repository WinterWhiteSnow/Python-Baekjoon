import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1063
# n_dict = {"R":[1,0],"L":[-1,0],"B":[0,-1],"T":[0,1]}
# import string
# str_str = list(string.ascii_uppercase)[:8]
# a,b,r = inputing().split()
# r = int(r)
# xa,ya = list(a)
# ya = int(ya)-1
# xa = str_str.index(xa)
# xb,yb = list(b)
# yb = int(yb)-1
# xb = str_str.index(xb)
# for _ in range(r):
#     move = list(inputing())
#     x,y = 0,0
#     for i in move:
#         a,b = n_dict[i]
#         x+=a
#         y+=b
#     if 0<=xa+x<=7 and 0<=ya+y<=7:
#         if xa+x == xb and ya+y == yb:
#             if 0<=xb+x<=7 and 0<=yb+y<=7:
#                 xa+=x
#                 ya+=y
#                 xb+=x
#                 yb+=y
#             else:
#                 continue
#         else:
#             xa+=x
#             ya+=y     
# print(str_str[xa]+str(ya+1))
# print(str_str[xb]+str(yb+1))







































