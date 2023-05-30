import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2636
# r,c = wow()
# n_list = [list(wow()) for _ in range(r)]
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# total = 0
# for y in range(r):
#     for x in range(c):
#         # print(y,x)
#         if n_list[y][x]:
#             total+=1
# def check(y,x):
#     global r,c
#     for yy,xx in move:
#         yyy,xxx = y+yy,xx+x
#         if 0<=yyy<r and 0<=xxx<c:
#             if n_list[yyy][xxx]:
#                 index_list.append((yyy,xxx))
# time = 0
# if total>0:
#     while True:
#         minus = 0
#         index_list = deque()
#         q = deque()
#         q.append((0,0))
#         m = deque()
#         m.append((0,0))
#         visit =  [[False]*c for _ in range(r)]
#         while q:
#             y,x = q.popleft()
#             for yy,xx in move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if visit[yyy][xxx] == False:
#                         visit[yyy][xxx]=True
#                         if n_list[yyy][xxx] == 0:
#                             m.append((yyy,xxx))
#                             q.append((yyy,xxx))
#         for y,x in m:
#             check(y,x)
#         if len(index_list)>0:
#             time+=1
        
#         for y,x in index_list:
#             if n_list[y][x]:
#                 n_list[y][x]=0
#                 minus+=1
#         if minus >0:
#             total-=minus
#             if total == 0:
#                 print(time,minus,sep="\n")
#         else:
#             break
# else:
#     print(0,0,sep="\n")

l = one()
n_list = deque(list(wow()))
max_max = 0
state_list = []
def go(index,list_list):
    global l,max_max,state_list
    # print("start!",index,list_list)
    if index < l:
        a = n_list[index]
        if list_list[-1]<a:
            go(index+1,list_list+[a])
        else:
            if len(list_list)>1:
                if list_list[-2]<a<list_list[-1]:
                    go(index+1,list_list[:-1]+[a])
                else:
                    go(index+1,list_list)
                    go(index+1,[a])
            else:
                go(index+1,list_list)
                go(index+1,[a])
    else:
        # print(l,list_list)
        ll = len(list_list)
        if ll > max_max:
            max_max=ll
            state_list=list_list

go(1,[n_list[0]])
print(max_max)
print(*state_list)
    







            
            

                
    














