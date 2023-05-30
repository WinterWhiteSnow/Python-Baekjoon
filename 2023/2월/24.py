import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1959
# r,c = wow()
# y,x = 0,0
# turn = 0
# if r%2 == 0:
#     if c%2 == 0:
#         gap = min(r//2-1,c//2-1)
#     else:
#         gap = min(r//2-1,c//2)
# elif c%2==0:
#     gap = min(r//2,c//2-1)
# else:
#     gap = min(r//2,c//2)
# y+=gap
# x+=gap
# turn+=gap*4
# r-=2*gap
# c-=2*gap
# # print(r,c,y,x,turn)
# if r==1:
#     print(turn)
#     if c == 1:
#         print(y+1,x+1)
#     else:
#         print(y+1,x+c)
# elif c==1:
#     print(turn+1)
#     print(y+r,x+1)
# else:
#     if r>2:
#         print(turn+3)
#     else:
#         print(turn+2)
#     print(y+2,x+1)








