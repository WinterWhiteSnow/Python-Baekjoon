import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2206
# r,c = map(int,input().split())
# n_list = [list(map(int,list(inputing()))) for _ in range(r)]
# if r==c==1:
#     print(1)
# else:
#     wall_list = deque()
#     visit = []
#     for _ in range(r):
#         v = []
#         for _ in range(c):
#             v.append([False,False])
#         visit.append(v)
#     move = [(1,0),(-1,0),(0,1),(0,-1)]
#     d = False
#     def bfs():
#         global r,c,d
#         q = deque()
#         visit[0][0][1]=1
#         q.append((0,0,1,1))
#         while q:
#             y,x,state,index = q.popleft()
#             for yy,xx in move:
#                 yyy,xxx = yy+y,xx+x
#                 if 0<=yyy<r and 0<=xxx<c:
#                     if n_list[yyy][xxx]:
#                         if state:
#                             if visit[yyy][xxx][0] == False:
#                                 visit[yyy][xxx][0] = index+1
#                                 q.append((yyy,xxx,0,index+1))
#                             else:
#                                 if visit[yyy][xxx][0]>index+1:
#                                     visit[yyy][xxx][0] = index+1
#                                     q.append((yyy,xxx,0,index+1))
#                     else:
#                         if visit[yyy][xxx][state] == False:
#                             visit[yyy][xxx][state] = index+1
#                             q.append((yyy,xxx,state,index+1))
#                         else:
#                             if visit[yyy][xxx][state]>index+1:
#                                 visit[yyy][xxx][state] = index+1
#                                 q.append((yyy,xxx,state,index+1))    
#     bfs()
#     a,b = visit[r-1][c-1]
#     if a==b==False:
#         print(-1)
#     else:
#         if a==b:
#             print(min(a,b))
#         else:
#             if a != False:
#                 print(a)
#             else:print(b)
    
#https://www.acmicpc.net/problem/9466        

def bfs(num):
    global l
    q = deque()
    q.append(num)
    index_list = [num]
    check = False
    v = []
    for i in visit:
        v.append(i)
    v[num]=True
    while q:
        index = q.popleft()
        next_index = total[index]
        if v[next_index] == False:
            q.append(next_index)
            v[next_index]=True
            index_list.append(next_index)
        else:
            if next_index in index_list:
                start = index_list.index(next_index)
                check=True
            break
    # print("end",num,index_list,check)
    minus = 0
    if check:
        for i in range(start,len(index_list)):
            visit[index_list[i]]=True
            minus+=1
    return minus
for _ in range(one()):
    l = one()
    total = [0]*l
    visit = [0]*l
    number = l
    n_list = list(wow())
    for i in range(l):
        total[i]=n_list[i]-1
        # if total[i]==i:
        #     visit[i]=True
    # print(total)
    # print(visit)
    for i in range(l):
        # print("i",i)
        # print("v",visit[i])
        if visit[i]==False:
            number-=bfs(i)

        
    cnt = 0
    # print("end!",visit)
    # for i in range(l):
    #     if visit[i]==0:
    #         cnt+=1
    print(number)
# 9
# 8 3 4 5 6 7 4 1 3    














