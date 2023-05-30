import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())



#https://www.acmicpc.net/problem/1987
# r,l = wow()
# n_list = [list(inputing()) for _ in range(r)]
# cnt = 0
# move = [(0,1),(0,-1),(1,0),(-1,0)]
# visited = [False]*27
# def go(y,x,r,l,visited,count):
#     global cnt
#     global move
#     if cnt == min(r*l,26):
#         return
#     if 0<=y<=r-1 and 0<=x<=l-1:
#         if visited[ord(n_list[y][x])-ord("A")]== False:
#             count+=1
#             visited[ord(n_list[y][x])-ord("A")]=True
#             if cnt < count:
#                 cnt = count
#             for yy,xx in move:
#                 go(yy+y,xx+x,r,l,visited,count)
#             visited[ord(n_list[y][x])-ord("A")]=False
# go(0,0,r,l,visited,0)
# print(cnt)

from collections import deque
num = one()
if num == 0:
    print(0)
else:
    n_list = deque()
    for i in range(1,10):
        n_list.append([i])
    def go(str_str):
        print("start",str_str)
        global num
        n = str_str[-1]
        if len(n_list) >= num:
            return
        for i in range(n):
            n_list.append(str_str+[i])
        str_str[-1]=0
        index = -2
        while True:
            if str_str[index]+1 == 10:
                str_str[index]=0
            else:
                str_str[index]=str_str[index]+1
                break
        # print("wow")
        # print(str_str,str_str[:-1])
        go(str_str[:-1])


    go("1")
    print(n_list)
        














