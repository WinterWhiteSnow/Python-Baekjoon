import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/3190
# from collections import deque
# r = one()
# n_list = [[0]*r for _ in range(r)]
# d = ((0,1),(-1,0),(0,-1),(1,0))
# d_index = 0
# time = 0
# state = deque()
# state.append((0,0))
# visited = [[False]*r for _ in range(r)]
# visited[0][0]=True
# for _ in range(one()):
#     y,x = wow()
#     n_list[y-1][x-1]=1
# # for i in n_list:
# #     print(i)
# n_dict = {}
# for _ in range(one()):
#     a,b = inputing().split()
#     a = int(a)
#     n_dict[a]=b
# while True:
#     move = d[d_index]
#     move_y,move_x = move
#     head = state[-1]
#     temp = state.popleft()
#     # print(head)
#     y,x = head
#     y+=move_y
#     x+=move_x
#     time+=1
#     if time in n_dict:
#         if n_dict[time] == "L":
#             d_index+=1
#         else:
#             d_index-=1
#         d_index%=len(d)
#     if 0<=y<=r-1 and 0<=x<=r-1:
#         if visited[y][x]==False:
#             state.append((y,x))
#             visited[y][x]=True
#             if n_list[y][x] == 1:
#                 n_list[y][x]=0
#                 state.appendleft(temp)
#             else:
#                 y,x = temp
#                 visited[y][x]=False
#         else:
#             break
#     else:
#         break
#     # print(time,state)
# print(time)

#https://www.acmicpc.net/problem/14891
# from collections import deque
# n_list = [deque(list(inputing())) for _ in range(4)]
# # -1 시계반대(0->-1) 1 시계방향(-1->0)
# def left(index,d):
#     if n_list[index][2] != n_list[index+1][6]:
#         return d*(-1)
#     else:
#         return 0
# def right(index,d):
#     # print("wow!!!",index,d)
#     if n_list[index][6] != n_list[index-1][2]:
#         return d*(-1)
#     else:
#         return 0
    
# for _ in range(one()):
#     index,d = wow()
#     index-=1
#     # n_list[index].rotate(d)
#     list_list = [0]*4
#     list_list[index]=d
#     # for i in n_list:
#     #     print(i)
#     # print(list_list)
#     l = len(n_list[0])
#     for i in range(index-1,-1,-1):
#         # print(i,i+1)
#         dd = left(i,list_list[i+1])
#         list_list[i]=dd
#         # list_list[i]=left(i,list_list[i+1])
#     for i in range(index+1,4):
#         # print(i,i-1)
#         dd = right(i,list_list[i-1])
#         list_list[i]=dd
#         # list_list[i]=right(i,list_list[i-1])
#     for i in range(4):
#         if list_list[i] !=0:
#             n_list[i].rotate(list_list[i])
#     # print(list_list)
#     # if index == 1:
#     #     y,x = n_list[index-1][3],n_list[index][6]
#     #     if y==x:
#     #         pass
#     #     else:
#     #         n_list[index].rotate(d*(-1))
#     # elif index == 4:
#     #     y,x=n_list[index-1][6],n_list[index-2][3]
#     #     if y==x:
#     #         pass
#     #     else:
#     #         n_list[index-2].rotate(d*(-1))
#     # else:
#     #     y,x = n_list[index-1][3],n_list[index][6]
#     #     if y==x:
#     #         pass
#     #     else:
#     #         n_list[index].rotate(d*(-1))
#     #     y,x=n_list[index-1][6],n_list[index-2][3]
#     #     if y==x:
#     #         pass
#     #     else:
#     #         n_list[index-2].rotate(d*(-1))
# cnt = 0    
# cnt+=1 if n_list[0][0] == "1" else 0
# cnt+=2 if n_list[1][0] == "1" else 0
# cnt+=4 if n_list[2][0] == "1" else 0
# cnt+=8 if n_list[3][0] == "1" else 0
# print(cnt)  














