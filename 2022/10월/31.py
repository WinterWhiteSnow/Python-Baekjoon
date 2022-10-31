import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/14753
# l = one()
# n_list = list(wow())
# n_list.sort()
# a,b = n_list[-1]*n_list[-2],n_list[0]*n_list[1]
# print(max(a,a*n_list[-3],b,b*n_list[-1]))

#https://www.acmicpc.net/problem/17203
# l,r = wow()
# n_list = list(wow())
# zero_list = []
# for i in range(1,l):
#     zero_list.append(abs(n_list[i]-n_list[i-1]))
# # print(zero_list)
# for _ in range(r):
#     a,b = wow()
#     if a==b:
#         print(0)
#     else:
#         print(sum(zero_list[a-1:b-1]))

#https://www.acmicpc.net/problem/8891
# n_dict = {}

# for _ in range(one()):
#     a,b = wow()
#     for index in [a,b]:
#         if index not in n_dict:
#             cnt = 1
#             stack = 1
#             while cnt < index:
#                 cnt+=stack
#                 stack+=1
#             if cnt > index:
#                 stack-=1
#                 cnt-=stack
#             # print(index,cnt,stack)
#             start_x = 1
#             start_y = stack
#             # print(start_x,start_y)
#             if cnt != index:
#                 gap=index-cnt
#                 start_x+=gap
#                 start_y-=gap            
#             n_dict[index]=[start_x,start_y]
#     xx = n_dict[a][0]+n_dict[b][0]      
#     yy = n_dict[a][1]+n_dict[b][1]      
#     total = xx+yy
#     cnt = 1
#     stack = 1
#     while stack+1 != total:
#         cnt+=stack
#         stack+=1
#     x_index = 1
#     y_index = stack
#     gap = y_index-yy
#     print(cnt+gap)

# https://www.acmicpc.net/problem/16162
# l,a,d = wow()
# n_list = list(wow())
# list_list = []
# for i in n_list:
#     if len(list_list) == 0:
#         if i==a:
#             list_list.append(i)
#     else:
#         if (i-a)%d == 0:
#             if list_list[-1]+d==i:
#                 list_list.append(i)
#     # print(i,list_list)
# print(len(list_list))      

#https://www.acmicpc.net/problem/14612
# r,l = wow()
# n_list = []
# for _ in range(r):
#     list_list = inputing().split()
#     if len(list_list) == 1:
#         n_list = sorted(n_list,key=lambda x : (x[1],x[0]))
#     elif len(list_list) == 2:
#         a,b = list_list
#         b = int(b)
#         for i in range(len(n_list)):
#             # print(n_list[i],b)
#             if n_list[i][0] == b:
#                 del n_list[i]
#                 break
#     else:
#         a,b,c = list_list
#         b,c = int(b),int(c)
#         n_list.append([b,c])
#     # print("n_list",n_list)
#     if n_list:
#         for a in n_list:
#             print(a[0],end=" ")
#         print()
#     else:
#         print("sleep")

            
    













