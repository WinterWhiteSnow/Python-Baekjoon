import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/9372
# for _ in range(one()):
#     n,m= wow()
#     for _ in range(m):
#         a,b = wow()
#     print(n-1)

#https://www.acmicpc.net/problem/2578
# n_list = [list(wow()) for _ in range(5)]
# total = [0]*26
# for y in range(5):
#     for x in range(5):
#         index = n_list[y][x]
#         total[index]=(y,x)
# cnt = 0
# visit = [[False]*5 for _ in range(5)]
# m_list = [list(wow()) for _ in range(5)]
# count = 0
# for y in range(5):
#     for x in range(5):
#         index = m_list[y][x]
#         y_index,x_index = total[index]
#         visit[y_index][x_index]=True
#         cnt+=1
#         if cnt >= 12:
#             # if count == False:
#             #     for y in range(5):
#             #         check = 0
#             #         for x in range(5):
#             #             check+=visit[y][x]
#             #         if check == 5:
#             #             count+=1
#             #     for x in range(5):
#             #         check = 0
#             #         for y in range(5):
#             #             check+=visit[y][x]
#             #         if check==5:
#             #             count+=1
#             sero_check = 0
#             garo_check = 0
#             right = 0
#             left = 0
#             total_cnt = 0
#             for xx in range(5):
#                 # sero_check+=visit[y][xx]
#                 right+=visit[xx][xx]
#             for yy in range(5):
#                 # garo_check+=visit[yy][x]
#                 left+=visit[4-yy][yy]
#                 # print(4-yy,yy)
#             if right == 5:
#                 total_cnt+=1
#             if left == 5:
#                 total_cnt+=1
#             for sero in range(5):
#                 a = 0
#                 b = 0
#                 for garo in range(5):
#                     a+=visit[sero][garo]
#                     b+=visit[garo][sero]
#                 if a == 5:
#                     total_cnt+=1
#                 if b == 5:
#                     total_cnt+=1
#             # print(cnt,y,x,total_cnt)
#             # for i in visit:
#             #     print(*i)
#             if total_cnt >=3:
#                 print(cnt)
#                 exit()

#https://www.acmicpc.net/problem/9507
# total = [0]*(68)
# total[0]=1
# total[1]=1
# total[2]=2
# total[3]=4
# start = 4
# for _ in range(one()):
#     index = one()
#     if total[index] != False:
#         print(total[index])
#     else:
#         for i in range(start,index+1):
#             total[i]=total[i-1]+total[i-2]+total[i-3]+total[i-4]
#         start = index
#         print(total[index])

#https://www.acmicpc.net/problem/10158
# r,c = wow()
# y,x = wow()
# time = one()
# if r-y < time:
#     y_re = (time-(r-y))%(2*r)
#     y = r
# else:
#     y_re = 0
#     y+=time
# if c-x < time:
#     x_re = (time-(c-x))%(2*c)
#     x = c
# else:
#     x_re = 0
#     x+=time
# # print("end?",y_re,x_re,y,x)
# if y_re >r:
#     y_re-=r
#     y=0
#     y+=y_re
# else:
#     y-=y_re
# if x_re >c:
#     x_re-=c
#     x=0
#     x+=x_re
# else:
#     x-=x_re
# print(y,x)                   
                
                    
                    
            
            














