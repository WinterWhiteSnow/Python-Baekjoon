import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16234
# from collections import deque
# n,gap_min,gap_max = wow()
# n_list=[list(wow()) for i in range(n)]
# time = 0
# q = deque()
# q.append((0,0))
# move= [(1,0),(0,1),(-1,0),(0,-1)]
# def go(y,x):
#     global visited
#     index_list = []
#     q = deque()
#     q.append((y,x))
#     count = 0
#     while q:
#         y,x=q.popleft()
#         index_list.append((y,x))
#         visited[y][x]=True
#         count+=n_list[y][x]
#         for a,b in move:
#             yy,xx = y+a,x+b
#             if 0<=yy<=n-1 and 0<=xx<=n-1:
#                 s = n_list[yy][xx]
#                 if gap_min<=abs(s-n_list[y][x])<=gap_max:
#                     if visited[yy][xx] == False:
#                         q.append((yy,xx))
#                         visited[yy][xx]=True
#     index = count//len(index_list)
#     for y,x in index_list:
#         n_list[y][x]=index
#     if len(index_list) >1:
#         return True
#     else:
#         return False      
# while True:
#     visited = [[False]*n for i in range(n)]
#     check = "no"
#     for y in range(n):
#         for x in range(n):
#             if visited[y][x]==False:
#                 visited[y][x]=True
#                 if go(y,x):
#                     check = "yes"
#     # print(check,time)
#     # for i in n_list:
#     #     print(*i)
#     if check == "no":
#         break
#     time+=1
# print(time)

r,l = wow()
n_list = [list(wow()) for _ in range(r)]
move1 = [(0,0),(0,1),(0,2),(0,3)]        
move2 = [(0,0),(0,1),(1,0),(1,1)]        
move3 = [(0,0),(0,1),(-1,0),(-2,0)]        
move4 = [(0,0),(1,0),(1,1),(2,1)]        
move5 = [(0,0),(0,1),(0,2),(1,1)]        
move_list = [move1,move2,move3,move4,move5]           
count = 0
def swap(list_list):
    temp_list = []
    for y,x in list_list:
        temp_list.append((x*(-1),y*(-1)))
    return temp_list

def check(index_list,y,x):
    global r,l
    count1=0
    count2=0
    count3=0
    cnt1 = 0
    cnt2 = 0
    cnt3=0
    for move in index_list:
        # y_index,x_index = y+move[0],x+move[1]*(-1)
        yy,xx = y+move[0],x+move[1]
        yyy,xxx = y+move[0]*(-1),x+move[1]
        if 0<=yy<=r-1 and 0<=xx<=l-1:
            count2+=1
            cnt2+=n_list[yy][xx]
        # if 0<=y_index<=r-1 and 0<=x_index<=l-1:
        #     count1+=1
        #     cnt1+=n_list[y_index][x_index]
        if 0<=yyy<=r-1 and 0<=xxx<=l-1:
            count3+=1
            cnt3+=n_list[yyy][xxx]

    # print(count1,count2,y,x)
    if count1 != 4:
        cnt1=0
    if count2 != 4:
        cnt2=0
    if count3 != 4:
        cnt3=0
    return max(cnt1,cnt2,cnt3)
def go(list_list,y,x):
    global r,l
    global count
    for index_list in list_list:
        a = index_list
        b = swap(index_list)
        cnt = max(check(a,y,x),check(b,y,x))
        if count < cnt:
            count =cnt
for y in range(r):
    for x in range(l):
        go(move_list,y,x)
print(count)
        

        
        
        













