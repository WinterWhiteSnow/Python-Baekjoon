import sys
from collections import deque
inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/15486
# l = one()
# pay = [0]*(l+2)
# n_list = [list(wow()) for _ in range(l)]
# max_max=0
# for i in range(l):
#     day,price = n_list.pop()
#     day-=1
#     now = l-i
#     if now+day > l:
#         pay[now]=pay[now+1]
#         continue
#     else:
#         pay[now]=max(pay[now+1],price+pay[now+day+1])
#         if max_max<pay[now]:
#             max_max = pay[now]
# print(max_max)

#https://www.acmicpc.net/problem/1062
# from itertools import combinations
# import string
# r,k = wow()
# n_list = []
# state = 0
# lower_str = list(string.ascii_lowercase)
# new_str = []
# for i in range(26):
#     if lower_str[i] in ["a","n","t","i","c"]:
#         continue
#     new_str.append(lower_str[i])
# p = set(["a","n","t","i","c"])
# for _ in range(r):
#     a = inputing()
#     n_list.append(set(list(a)))
# if k <5:
#     print(0)
# else:
#     k-=5
#     check_list = list(combinations(new_str,r=k))
#     for f in check_list:
#         e = p.union(set(f))
#         cnt = 0
#         for n in n_list:
#             if len(n-e)==0:
#                cnt+=1
#         if state < cnt:
#             state = cnt 
#     print(state)

#https://www.acmicpc.net/problem/1331
# import string
# str_str = list(string.ascii_uppercase)            
# move = []
# n_dict = {}
# index=0
# y,x = False,False
# for i in str_str:
#     n_dict[i]=index
#     index+=1
# start_y,start_x = 0,0
# state = True
# index_list = []
# visit = [[0]*(6) for _ in range(6)]
# for d in range(36):
#     a,n = list(inputing())
#     a,n = n_dict[a],int(n)-1
#     # print(y,x,a,n,abs(y-a),abs(x-n))
#     if d == 0:
#         y,x = a,n
#         visit[y][x]=1
#         start_y,start_x = a,n
#     else:
#         if visit[a][n] == False:
#             if abs(y-a)==1:
#                 if abs(x-n) ==2:
#                     y,x = a,n
#                     visit[y][x]=True
#                     # index_list.append((a,n))
#                 else:
#                     state = False
#             elif abs(y-a)==2:
#                 # print("second!!",y,a,x,n)
#                 if abs(x-n)==1:
#                     y,x=a,n
#                     visit[y][x]=True
#                     # index_list.append((a,n))
#                 else:
#                     state=False
#             else:
#                 state=False
#         else:
#             # print(y,x,a,n,state)
#             state = False
#     if d == 35:
#         if state:
#             # print(start_y,start_x,x,y)
#             if abs(start_y-y)==2:
#                 if abs(start_x-x)==1:
#                     pass
#                 else:
#                     state = False
#             elif abs(start_y-y)==1:
#                 if abs(start_x-x)==2:
#                     pass
#                 else:
#                     state = False
#             else:
#                 state= False
#     # print(y,x,a,n,state)
# # index_list.sort(key=lambda x : (x[0],x[1]))
# # print(index_list)
# # for i in visit:
# #     print(*i)
# print("Valid"if state else "Invalid") 














        
        
        
        










