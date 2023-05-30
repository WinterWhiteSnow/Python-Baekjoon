import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17140
# y,x,k = wow()
# y,x = y-1,x-1
# n_list = [list(wow()) for _ in range(3)]
# r,l = 3,3
# # print(n_list[y][x],k)
# time = 0
# while True: #x>=l or y>=r or n_list[y][x]!=k
#     if time == 101:
#         break
#     if 0<=y<r and 0<=x<l:
#         # print("here!!!",n_list[y][x],k)
#         if n_list[y][x] == k:
#             print(time)
#             exit()
#     time+=1
#     # print("start",r,l,n_list)
#     index = "none"
#     if r>=l:
#         index=0
#         list_list = []
#         max_l = 0
#         for i in n_list:
#             n_dict = {}
#             for a in i:
#                 if a not in n_dict:
#                     n_dict[a]=1
#                 else:
#                     n_dict[a]+=1
#             n = list(n_dict.items())
#             n.sort(key=lambda x: (x[1],x[0]))
#             # print("n",n)
#             m = []
#             for i in n:
#                 if i[0] != 0:
#                     m.extend(i)
#             if len(m) > max_l:
#                 max_l=len(m)
#             # print("m",m)
#             list_list.append(m)
#         for i in range(len(list_list)):
#             list_list[i]+=[0]*(max_l-len(list_list[i]))
#         n_list=list_list
#     else:   
#         index = 0
#         n_dict = {}
#         max_r = 0
#         for i in range(r):
#             list_list = n_list[i]
#             for ii in range(l):
#                 if ii not in n_dict:
#                     n_dict[ii]=[list_list[ii]]
#                 else:
#                     n_dict[ii]+=[list_list[ii]]
#         # print("wow!!!",n_dict)
#         m_list = []
#         for i in n_dict.values():
#             m_list.append(i)
#         n_list = m_list
#         m_dict = {}
#         for i in n_list:
#             n_dict = {}
#             for a in i:
#                 if a not in n_dict:
#                     n_dict[a]=1
#                 else:
#                     n_dict[a]+=1
#             n = list(n_dict.items())
#             n.sort(key=lambda x: (x[1],x[0])) #등장, 그 수
#             m = []
#             for i in n:
#                 if i[0] != 0:
#                     m.extend(i)
#             # print(m)
#             if max_r < len(m):
#                 max_r = len(m)
#             # if time == 5:
#             #     print(m)
#             m_dict[index]=m
#             index+=1
#             # for i in range(len(m)):
#             #     if i not in m_dict:
#             #         m_dict[i]=[m[i]]
#             #     else:
#             #         m_dict[i]+=[m[i]]
#         m_list = list(m_dict.values())
#         temp_list = [[0]*len(m_dict) for _ in range(max_r)]
#         # print(time,m_dict)
#         # for i in m_list:
#         #     if len(i)>max_l:
#         #         max_l=len(i)
#         # for i in temp_list:
#         #     print(*i)
#         for kk in m_dict.keys(): #x값
#             for yy in range(len(m_dict[kk])):
#                 temp_list[yy][kk]=m_dict[kk][yy]
#         # for i in range(len(m_list)):
#         #     m_list[i]+=[0]*(max_l-len(m_list[i]))
#         n_list = temp_list
#     r = len(n_list)
#     l = len(n_list[0])
#     if r >= 100:
#         n_list = n_list[:100]
#         r=100
#     if l >= 100:
#         for i in range(r):
#             n_list[i]=n_list[i][:100]
#         l = 100
#     # print(time)
#     # for i in n_list:
#     #     print(i)
#     # if time == 5:
#     #     break
#     # print(r,l,len(n_list),len(n_list[0]))
# print(-1)
















