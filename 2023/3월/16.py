import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1600
# k = one()
# c,r = wow()
# n_list = [list(wow()) for _ in range(r)]
# move = [(-2,-1),(-1,-2)]
# visit = [[[0]*c for _ in range(r)] for _ in range(k+1)]
# for i in range(2):
#     y,x = move[i]
#     move.append((y,-x))
# for i in range(4):
#     y,x = move[i]
#     move.append((-y,x))
# nomal=[(1,0),(0,1),(-1,0),(0,-1)]
# visit[k][0][0]=1
# def bfs(): # move == horse
#     global k,c,r
#     cnt = 0
#     q = deque()
#     q.append((k,0,0))
#     while q:
#         state,y,x = q.popleft()
#         index = visit[state][y][x]
#         # print("start!!",state,y,x,index)
#         if y==r-1 and x==c-1:
#             print(visit[state][y][x]-1)
#             return
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if n_list[yyy][xxx ] == False:
#                     if state>0:
#                         if visit[state-1][yyy][xxx] == False:
#                             visit[state-1][yyy][xxx]=index+1
#                             q.append((state-1,yyy,xxx))
#                         elif visit[state-1][yyy][xxx]>index+1:
#                             visit[state-1][yyy][xxx]=index+1
#                             q.append((state-1,yyy,xxx))
#         for yy,xx in nomal:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<r and 0<=xxx<c:
#                 if n_list[yyy][xxx] == False:
#                     if visit[state][yyy][xxx] == False:
#                         visit[state][yyy][xxx]=index+1
#                         q.append((state,yyy,xxx))
#                     elif visit[state][yyy][xxx]>index+1:
#                         visit[state][yyy][xxx]=index+1
#                         q.append((state,yyy,xxx))   
#         # print("mid,end",y,x)
#         # print(q)    
#     print(-1)
#     return
# bfs()

#https://www.acmicpc.net/problem/2146
# n = one()
# n_list = [list(wow()) for _ in range(n)]
# visit = [[False]*n for _ in range(n)]
# index_list = []
# move = [(1,0),(-1,0),(0,1),(0,-1)]
# def bfs(y,x):
#     global n
#     list_list = [(y,x)]
#     q = deque()
#     q.append((y,x))
#     while q:
#         y,x = q.popleft()
#         for yy,xx in move:
#             yyy,xxx = yy+y,xx+x
#             if 0<=yyy<n and 0<=xxx<n:
#                 if n_list[yyy][xxx]:
#                     if visit[yyy][xxx]==False:
#                         list_list.append((yyy,xxx))
#                         visit[yyy][xxx]=True
#                         q.append((yyy,xxx))
#     index_list.append(list_list)
# for y in range(n):
#     for x in range(n):
#         if n_list[y][x]:
#             if visit[y][x]==False:
#                 visit[y][x]=True
#                 bfs(y,x)
# l= len(index_list)
# total = 1000000000000000000001
# for start in range(l-1):
#     for end in range(start+1,l):
#         a = index_list[start]
#         b = index_list[end]
#         gap = 1000000000000000001
#         for aa in a:
#             for bb in b:
#                 y,x = aa
#                 yy,xx = bb
#                 c = abs(y-yy)+abs(x-xx)
#                 if gap > c:
#                     gap = c
#         if total>gap-1:
#             total=gap-1
# print(total)

#https://www.acmicpc.net/problem/16920
index_list = []
r,c,p = wow()
index_list = deque()
for _ in range(p):
    index_list.append(deque())
m_list = list(wow())
visit = [[False]*c for _ in range(r)]
n_list = [list(inputing()) for _ in range(r)]
move = [(-1,0),(1,0),(0,1),(0,-1)]
count = [0]*(p+1)
for y in range(r):
    for x in range(c):
        if n_list[y][x] != ".":
            if n_list[y][x] == "#":
                visit[y][x]=True
                continue
            index = int(n_list[y][x])
            index_list[index-1]+=[(y,x)]
            count[index]+=1
            visit[y][x]=True
# print("start!",count)
def check_bfs(q,index):
    temp_list = deque()
    # print("repeat",q)
    while q:
        y,x = q.popleft()
        # index = int(n_list[y][x])
        # print("start!!!",y,x,index,q)
        for yy,xx in move:
            yyy,xxx = yy+y,xx+x
            if 0<=yyy<r and 0<=xxx<c:
                if visit[yyy][xxx]==False:
                    visit[yyy][xxx]=index
                    temp_list.append((yyy,xxx))
                    count[index]+=1
    return temp_list
        
        
def bfs(index_list):
    global r,c,p
    while index_list:
        return_list = deque()
        index = 1
        no = 0
        while index_list:
            repeat = m_list[index-1]-1
            q = index_list.popleft()
            temp_list = deque()
            # print("re",index,q)
            while q:
                y,x = q.popleft()
                # index = int(n_list[y][x])
                # print("start!!!",y,x,index,q)
                for yy,xx in move:
                    yyy,xxx = yy+y,xx+x
                    if 0<=yyy<r and 0<=xxx<c:
                        if visit[yyy][xxx]==False:
                            visit[yyy][xxx]=index
                            temp_list.append((yyy,xxx))
                            count[index]+=1
            for _ in range(repeat):
                if len(temp_list)>0:
                    temp_list = check_bfs(temp_list,index)
                    repeat-=1
                else:
                    break
            return_list.append(temp_list)
            index+=1
            if len(temp_list) == 0:
                no+=1
        # print(no)
        # for i in visit:
        #     print(i)
        if no != p:
            index_list=return_list
        else:
            return                            
bfs(index_list)
print(*count[1:])
# for i in visit:
#     print(i)









