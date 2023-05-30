import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17406
# from collections import deque
# n,m,k = wow()
# n_list = [list(wow()) for _ in range(n)]
# move=[(0,1),(1,0),(0,-1),(-1,0)]
# k_list = [list(wow()) for _ in range(k)]
# k_visit = [False]*k
# count = 100000000000000000000000000001
# def go(n_list,k_visit,index,cnt):
#     global m,n,k,count
#     r,c,s = k_list[index]
#     # print(k_visit,m,n)
#     # print(r,c,s)
#     m_list = []
#     for i in n_list:
#         mm = []
#         for a in i:
#             mm.append(a)
#         m_list.append(mm)
#     m_visit = [[False]*m for _ in range(n)]
#     start_y,start_x = r-s-1,c-s-1
#     end_y,end_x = r+s-1,c+s-1
#     # print(start_y,end_y,start_x,end_x)
#     move_index= 0
#     # print("now")
#     # print(*m_list,sep="\n")
#     for _ in range((end_y-start_y)//2):
#         y,x = start_y,start_x
#         index_list = deque()
#         num_list = deque()
#         index_list.append((y,x))
#         num_list.append(m_list[y][x])
#         for move_index in range(4):
#             # print(move_index,"Start!!!",y,x)
#             while True:
#                 yy,xx = move[move_index]
#                 yyy,xxx = y+yy,x+xx
#                 if start_y<=yyy<=end_y and start_x<=xxx<=end_x:
#                     y,x=yyy,xxx
#                 else:
#                     break
#                 index_list.append((y,x))
#                 num_list.append(m_list[y][x])
#         index_list.pop()
#         num_list.pop()
#         # index_list.rotate(1)
#         num_list.rotate(1)
#         num_index = 0
#         for y_index,x_index in index_list:
#             m_list[y_index][x_index]=num_list[num_index]
#             num_index+=1
#         start_y,start_x=start_y+1,start_x+1
#         end_y,end_x= end_y-1,end_x-1
#         # print("end")
#         # print(*m_list,sep="\n")
#         # print(*index_list,sep="\n")
#         # print(num_list)
#         # exit()
#     if cnt == k:
#         for i in range(n):
#             total = sum(m_list[i])
#             if count > total:
#                 count = total
#         return
#     for i in range(k):
#         if k_visit[i]==False:
#             k_visit[i]=True
#             go(m_list,k_visit,i,cnt+1)
#             k_visit[i]=False               
# for i in range(k):
#     k_visit[i]=True
#     go(n_list,k_visit,i,1)
#     k_visit[i]=False
# print(count)

    










