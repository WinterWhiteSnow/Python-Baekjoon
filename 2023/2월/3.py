import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/21735
# l,k = wow()
# n_list = [1]+list(wow())
# cnt = 0
# visited = [False]*(l+1)
# def go(index,count,total,visited,record):
#     global k
#     global cnt
#     global l
#     # print("start!!",index)
#     # print("record",record,count)
#     # print("start",index,count,total)
#     if count == k+1:
#         # print("wow!!",index,total,count)
#         # print(visited)
#         if cnt < total:
#             cnt = total
#         return
#     if index <=l:
#         if visited[index] == False:
#             visited[index]=True
#             total+=n_list[index]
#             record.append(total)
#             count+=1
#             go(index+1,count,total,visited,record)
#             go(index+2,count,total//2,visited,record)
#             record.pop()
#             count-=1
#             total-=n_list[index]
#             visited[index]=False
#     else:
#         if cnt < total:
#             cnt = total
#         return
# go(0,0,0,visited,[])
# print(cnt)

#https://www.acmicpc.net/problem/26169
# n_list = [list(wow()) for _ in range(5)]
# r,l = wow()
# visited = [[False]*5 for _ in range(5)]
# for y in range(5):
#     for x in range(5):
#         if n_list[y][x]==-1:
#             visited[y][x]=True
# check = "no"
# def go(y,x,count,total,visited):
#     global check
#     # print("Start",y,x,count,total)
#     if count == 4:
#         if total >= 2:
#             check = "yes"
#         return
#     if total >=2:
#         check = "yes"
#         return
#     if 0<=y<=4 and 0<=x<=4:
#         if visited[y][x] == False:
#             visited[y][x]=True
#             if n_list[y][x] == 1:
#                 total+=1
#             count+=1
#             go(y+1,x,count,total,visited)            
#             go(y-1,x,count,total,visited)            
#             go(y,x+1,count,total,visited)            
#             go(y,x-1,count,total,visited)            
#             count-=1
#             visited[y][x]=False
#             if n_list[y][x]==1:
#                 total-=1
# go(r,l,0,0,visited)
# print(0 if check=="no" else 1)

#https://www.acmicpc.net/problem/25328
from itertools import permutations
a = list(inputing())
b = list(inputing())
c = list(inputing())
k = one()
a = set(permutations(a,r=k))
b = set(permutations(b,r=k))
c = set(permutations(c,r=k))
x,y,z = set(a&b),set(b&c),set(a&c)
r = set(list(map("".join,(map(sorted,list(x | y|z))))))
if r:
    r = sorted(list(r))
    print(*r,sep="\n")
else:
    print(-1)








