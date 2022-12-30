import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17626
# zero_list = [0]*(50001)
# for i in range(1,int(50000**(1/2))+1):
#     zero_list[i**2]=1
#     # print(i**2)
# for i in range(2,50001):
#     if zero_list[i] != 0:
#         continue
#     zero_list[i]=zero_list[i-1]+1
#     for a in range(1,int(i**(1/2))+1):
#         zero_list[i]=min(zero_list[i],zero_list[a**2]+zero_list[i-a**2])
# print(zero_list[one()])

#https://www.acmicpc.net/problem/10844
# l = one()
# if l == 1:
#     print(9)
# else:
#     n_list=[]
#     for i in range(1,9):
#         a = [i,i+1]
#         if a not in n_list:
#             n_list.append(a)
#         if a[::-1] not in n_list:
#             n_list.append(a[::-1])
#         b = [i,i-1]
#         if b[0] == 0:
#             continue
#         if b not in n_list:
#             n_list.append(b)
#         b = b[::-1]
#         if b[0] == 0:
#             continue
#         if b not in n_list:
#             n_list.append(b)
#     #     print(n_list)
#     # print(sorted(n_list,key=lambda x: x[-1]))
#     n_dict = {}
#     for i in n_list:
#         num = i[-1]
#         if num not in n_dict:
#             n_dict[num]=1
#         else:
#             n_dict[num]+=1
#     # print(n_dict)
#     key = 2
#     for _ in range(l-key):
#         new_dict = {}
#         for i in range(10):
#             new_dict[i]=0
#         for i in range(10):
#             if i == 9:
#                 new_dict[i-1]+=n_dict[i]
#             elif i == 0:
#                 new_dict[i+1]+=n_dict[i]
#             else:
#                 new_dict[i-1]+=n_dict[i]
#                 new_dict[i+1]+=n_dict[i]
#         n_dict = new_dict
#     print(sum(n_dict.values())%1000000000)

# https://www.acmicpc.net/problem/11048
# r,l= wow()
# n_list = [list(wow()) for _ in range(r)]
# # n_list[0][1]=n_list[0][1]+n_list[0][0]
# # n_list[1][0]=n_list[1][0]+n_list[0][0]
# max_max = 0
# for y in range(r):
#     for x in range(l):
#         cnt = n_list[y][x]
#         list_list = [cnt]
#         if 0<=x-1<=l-1:
#             x1,y1 = x-1,y
#             index1 = cnt+n_list[y1][x1]
#             list_list.append(index1)
#         if 0<=y-1<=r-1:
#             x2,y2 = x,y-1
#             index2 = cnt+n_list[y2][x2]
#             list_list.append(index2)
#         if 0<=x-1<=l-1 and 0<=y-1<=r-1:
#             x3,y3 = x-1,y-1
#             index3 = cnt+n_list[y3][x3]
#             list_list.append(index3)
        
#         n_list[y][x]=max(list_list)
#         max_max=max(max_max,n_list[y][x])
#         # print(x)
#         # for i in n_list:
#         #     print(*i)
# print(max_max)
        
    









