import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/24268
# from itertools import permutations
# n,d = wow()
# nn = n
# a_list = []
# while nn != 0:
#     a_list.append(nn%d)
#     nn//=d
# # print(a_list)
# n_list = [i for i in range(d)]
# reverse_list = sorted(n_list)
# count = 0
# for i in range(d):
#     count+=d**i*reverse_list[i]
# if n > count:
#     print(-1)
# else:
#     new_list = list(permutations(n_list,r=d))
#     # print(new_list)
#     list_list = []
#     for i in new_list:
#         if i[-1] == 0:
#             pass
#         else:
#             index = 0
#             cnt = 0
#             # i =i[::-1]
#             for a in i:
#                 cnt+=d**index*a
#                 index+=1
#             list_list.append(cnt)
#             # print(i,cnt)
#     # print(sorted(list_list))
#     list_list = [i for i in list_list if i>n]
#     if len(list_list) > 0:
#         print(min(list_list))
#     else:
#         print(-1)

#https://www.acmicpc.net/problem/2502
# k,total = wow()
# n_list = ["x","y"]
# while len(n_list) < k:
#     n_list.append(n_list[-1]+n_list[-2])
# y,x = n_list[-1].count("y"),n_list[-1].count("x")
# for a in range(1,total//x+1):
#     for b in range(1,total//y+1):
#         if x*a+y*b == total:
#             print(a)
#             print(b)
#             exit()
#             # print(x*a+y*b)
#             # exit()

#https://www.acmicpc.net/problem/16173
# r =one()
# n_list = [list(wow()) for _ in range(r)]
# def go(y,x,list_list,r):
#     if 0<=y<=r-1 and 0<=x<=r-1:
#         if y==r-1 and x==r-1:
#             print("HaruHaru")
#             exit()
#         move = list_list[y][x]
#         if move > 0:
#             # for down in range(1,move+1):
#                 go(y+move,x,list_list,r)
#             # for right  in range(1,move+1):
#                 go(y,x+move,list_list,r)
# go(0,0,n_list,r)
# print("Hing")

#점프왕 쩰리 (large)
# from collections import deque
# r =one()
# n_list = deque(deque(wow()) for _ in range(r))
# visited = [[False]*r for _ in range(r)]
# # print(n_list)
# def go(y,x,list_list,r,visited):     
#     if 0<=y<=r-1 and 0<=x<=r-1:
#         if not visited[y][x]: 
#             visited[y][x]=True
#             move = list_list[y][x]
#             if move == -1:
#                 sys.stdout.write("HaruHaru")
#                 exit()
#             if move > 0:
#                 go(y+move,x,list_list,r,visited)
#                 go(y,x+move,list_list,r,visited)
# go(0,0,n_list,r,visited)
# sys.stdout.write("Hing")

from collections import deque
l = one()
n_list = deque(wow())
minus = deque([0])
plus = deque([0])
n_dict = {}
num_list = set(i for i in range(1,sum(n_list)+1))
def go(minus,plus,list_list):
    # print(minus,plus,list_list)
    m = deque(i for i in minus)
    p = deque(i for i in plus)
    temp_list = deque(i for i in list(list_list))
    y = sum(minus)
    x = sum(plus)
    index =y-x
    if index > 0:
        n_dict[index]=1
    if len(temp_list) > 0:
        a = temp_list.popleft()
        go(m+deque([a]),p,temp_list)
        go(m,p+deque([a]),temp_list)
        for _ in range(len(temp_list)):
            temp_list.rotate()
            go(m+deque([a]),p,temp_list)
            go(m,p+deque([a]),temp_list)
            
go(minus,plus,n_list)
for _ in range(l-1):
    n_list.rotate(-1)
    go(minus,plus,n_list)
sys.stdout.write(len(num_list-set(n_dict.keys())))
    

                
            








