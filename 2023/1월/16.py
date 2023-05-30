import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/14889
# r = one()
# n_list = []
# visited = [False]*(r+1)
# for _ in range(r):
#     list_list = list(wow())
#     n_list.append(list_list)
# min_min = 100001

# def go(r,cnt_list,cnt,n_list,visited):
#     global min_min
#     # print(visited)
#     # print(cnt_list,r)
#     if cnt != r//2:
#         if cnt_list[-1] < r:
#             for ii in range(cnt_list[-1],r+1):
#                 visit = [i for i in visited]
#                 if visit[ii] == False:
#                     list_list = [i for i in cnt_list]
#                     list_list.append(ii)
#                     visit[ii]=True
#                     go(r,list_list,cnt+1,n_list,visit)
#     else:
#         # print(cnt_list)
#         start_score = 0
#         link_score = 0
#         for y in range(1,r+1):
#             for x in range(y+1,r+1):
#                 y_index= y-1
#                 x_index= x-1
#                 if visited[y]==visited[x]==True:
#                     start_score+=n_list[y_index][x_index]
#                     start_score+=n_list[x_index][y_index]
#                 elif visited[y]==visited[x]==False:
#                     link_score+=n_list[y_index][x_index]
#                     link_score+=n_list[x_index][y_index]
#         min_min = min(min_min,abs(start_score-link_score))
#         if min_min == 0:
#             print(0)
#             exit()
# for i in range(1,r+1):  
#     visit = [i for i in visited]
#     visit[i]=True        
#     go(r,[i],1,n_list,visit)
# print(min_min)

n_list = []
zero_cnt = 0
for _ in range(9):
    a = list(wow())
    n_list.append(a)
    zero_cnt+=a.count(0)
check_list = []

for y in range(0,9,3):
    for x in range(0,9,3):
        quadra_check = [[False]*3 for _ in range(3)]
        paint_list = [False]*10
        # qq_list = []
        index_list = []
        for y_index in range(y,y+3):
            q_list = []
            for x_index in range(x,x+3):
                yy = y_index%3
                xx = x_index%3
                q_list.append(n_list[y_index][x_index])
                if n_list[y_index][x_index] != 0:
                    quadra_check[yy][xx]=True
                    paint_list[n_list[y_index][x_index]]=True
                else:
                    index_list.append([y_index,x_index])
            # qq_list.append(q_list) 
        check_list.append([paint_list,index_list])      
        # print(quadra_check)
# print("wow")
# for i in n_list:
#     print(*i)
# print(check_list)
def go(n_list,zero_cnt,check_list):
    # print(zero_cnt)
    # if zero_cnt<20:
    #     for i in n_list:
    #         print(*i)
    if zero_cnt != 0:
        for i in range(len(check_list)):
            start_list = check_list[i]
            paint_list = start_list[0]
            index_list = start_list[1]
            for index in range(len(index_list)):
                y,x = index_list[index]      
                sero_check = [False]*10 #x 그대로
                garo_check = [False]*10 #y 그대로
                for move in range(9):
                    answer = n_list[move][x]
                    sero_check[answer]=True
                    bnswer = n_list[y][move]
                    garo_check[bnswer]=True
                # print(sero_check)
                # print(garo_check)
                for ii in range(1,10):
                    if paint_list[ii]==sero_check[ii]==garo_check[ii]==False:
                        new_list = []
                        for a in n_list:
                            temp_list=[]
                            for aa in a:
                                temp_list.append(aa)
                            new_list.append(temp_list)
                        new_list[y][x]=ii
                        paint = [a for a in paint_list]
                        paint[ii]=True
                        zz = zero_cnt
                        zz-=1
                        iiii = [a for a in index_list]
                        iiii.remove(iiii[index])
                        check = [a for a in check_list]
                        check[i]=[paint,iiii]
                        go(new_list,zz,check)
    else:
        for i in n_list:
            print(*i)
        exit()
            # check = [i for i in check_list]
            # check[i]=[paint_list,index_list]
    # print(check_list)
go(n_list,zero_cnt,check_list)

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0


