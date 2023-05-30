import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/14500
# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# move1 = [(0,0),(0,1),(0,2),(0,3)]        
# move2 = [(0,0),(0,1),(1,0),(1,1)]        
# move3 = [(0,0),(0,1),(-1,0),(-2,0)]        
# move4 = [(0,0),(1,0),(1,1),(2,1)]        
# move5 = [(0,0),(0,1),(0,2),(1,1)]        
# move_list = [move1,move2,move3,move4,move5]           
# count = 0
# def swap(list_list):
#     temp_list = []
#     for y,x in list_list:
#         temp_list.append((x,y))
#     return temp_list

# def check(index_list,y,x):
#     global r,l
#     count1=0
#     count2=0
#     count3=0
#     count4=0
#     cnt1 = 0
#     cnt2 = 0
#     cnt3=0
#     cnt4=0
#     for move in index_list:
#         y_index,x_index = y+move[0],x+move[1]*(-1)
#         yy,xx = y+move[0],x+move[1]
#         yyy,xxx = y+move[0]*(-1),x+move[1]
#         yyyy,xxxx = y+move[0]*(-1),x+move[1]*(-1)
#         if 0<=yy<=r-1 and 0<=xx<=l-1:
#             count2+=1
#             cnt2+=n_list[yy][xx]
#         if 0<=y_index<=r-1 and 0<=x_index<=l-1:
#             count1+=1
#             cnt1+=n_list[y_index][x_index]
#         if 0<=yyy<=r-1 and 0<=xxx<=l-1:
#             count3+=1
#             cnt3+=n_list[yyy][xxx]
#         if 0<=yyyy<=r-1 and 0<=xxxx<=l-1:
#             count4+=1
#             cnt4+=n_list[yyyy][xxxx]

#     # print(count1,count2,y,x)
#     if count1 != 4:
#         cnt1=0
#     if count2 != 4:
#         cnt2=0
#     if count3 != 4:
#         cnt3=0
#     if count4 != 4:
#         cnt4 = 4
#     return max(cnt1,cnt2,cnt3,cnt4)
# def go(list_list,y,x):
#     global r,l
#     global count
#     for index_list in list_list:
#         a = index_list
#         b = swap(index_list)
#         cnt = max(check(a,y,x),check(b,y,x))
#         if count < cnt:
#             count =cnt
# for y in range(r):
#     for x in range(l):
#         go(move_list,y,x)
# print(count)

from collections import deque
r,l = wow()
n_list = [list(wow()) for _ in range(r)]
move1 = [(0,1)]
move2 = [(0,-1),(0,1)]
move3 = [(0,1),(-1,0)]
move4 = [(0,1),(-1,0),(0,-1)]
move5 = [(0,1),(-1,0),(0,-1),(1,0)]
move_list = [move1,move2,move4,move3,move5]
index_list = []
total = 0
visited = [[False]*l for _ in range(r)]
for y in range(r):
    for x in range(l):
        z = n_list[y][x]
        if z != 0 and z != 6:
            index_list.append((y,x))
        else:
            total+=1
            if z == 6:
                visited[y][x]=True
for i in index_list:
    y,x = i
    visited[y][x]=True
    total-=1
cnt = 1000001
def go(index_list,index,visited,total):
    global r,l
    global cnt
    # print("Start!!!")
    # for i in visited:
    #     print(*i)
    if index ==len(index_list):
        # count = 0
        # for y in range(r):
        #     for x in range(l):
        #         if visited[y][x]==False:
        #             count+=1
        # if cnt > count:
        #     cnt = count
        print("wow!")
        for i in visited:
            print(*i)
        if cnt > total:
            cnt = total
        return
    for i in range(4):
        visit = []
        for a in visited:
            c = []
            for b in a:
                c.append(b)
            visit.append(c)
        total_total = total
        # print(index,index_list,index_list[index])
        y,x = index_list[index]
        ind = n_list[y][x]
        move_index = move_list[ind-1]
        # print("move!@!!",move_index)
        for move in move_index:
            move_y,move_x = move
            if i == 1:
                move_x,move_y = move_y,move_x
            elif i == 2:
                move_x = move_x*(-1)
                move_y = move_y*(-1)
            elif i == 3:
                move_x,move_y = move_y,move_x
                move_x = move_x*(-1)
                move_y = move_y*(-1)
            # print("move",move_y,move_x,y,x)
            q = deque()
            q.append((y,x))
            while True:
                yy,xx = q.popleft()
                yyy,xxx = yy+move_y,xx+move_x
                # print("yy,xx",yy,xx)
                if 0<=yyy<= r-1 and 0<=xxx<=l-1:
                    if visit[yyy][xxx]==False:
                        visit[yyy][xxx]=True
                        total_total-=1
                        q.append((yyy,xxx))
                    else:
                        q.append((yyy,xxx))
                else:
                    break
                print("q",q)
        index+=1
        go(index_list,index,visit,total_total)
        index-=1
go(index_list,0,visited,total)
print(cnt)        
            
                            
                        
                            
                        
                    
                
                    
            










