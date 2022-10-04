import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#회의실배정 1931
# l = one()
# n_dict = {}
# for _ in range(l):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=b
#     else:
#         n_dict[a]=min(n_dict[a],b)
# list_list = list(n_dict.items())
# list_list.sort(key=lambda x : x[1],reverse=True)          
# list_list.sort(key=lambda x : x[0])
# 해당 중복검사는 l=3 [8,8]*3 을 1로 반환하게만듦, 정답은 3(시작과 동시에 끝이 허용되니)
# n_list = []
# list_list = [list(wow()) for _ in range(l)]
# list_list.sort(key=lambda x : x[1])
# list_list.sort(key=lambda x: x[0])
# for index in range(len(list_list)):
#     if len(n_list) == 0:
#         n_list.append(list_list[index])
#     else:
#         x,y = n_list[-1]
#         a,b = list_list[index]
#         if x<=a and y>b:
#             n_list[-1]=[a,b]
#         else:
#             if y<=a:
#                 n_list.append([a,b])
#     # print(n_list)
# print(len(n_list))

#1697
# sys.setrecursionlimit(10**7)
# aa,bb = wow()
# if aa>=bb:
#     print(aa-bb)
# else:
#     n_list = [0]*(max(aa,bb)+3)
#     index=0
#     count = 0
#     a,b = min(aa,bb),max(aa,bb)
#     def search(x,y,cnt):
#         if n_list[y] == 0:
#             n_list[y]=cnt
#         else:
#             n_list[y]=min(n_list[y],cnt)
#         if n_list[x] == 0:
#             n_list[x]=n_list[y]+abs(x-y)
#         else:
#             n_list[x]=min(n_list[x],n_list[y]+abs(x-y))
#         if y==0:
#             return
#         # print(n_list[a:b+2],y,cnt)
#         if y%2:
#             if y == 1:
#                 search(x,0,cnt+1)
#             else:
#                 search(x,y+1,cnt+1)
#                 search(x,y-1,cnt+1)
#         else:
#             search(x,y//2,cnt+1)
#     search(a,b,index)
#     # print(n_list)
#     print(n_list[a])

r,l = wow()
n_list = [list(inputing()) for _ in range(r)]
def bfs(x,y,count):
    if 0<=x<=l-1 and 0<=y<=r-1:
        for i in n_list:
            print(*i)
        if n_list[y][x] == "1":
            n_list[y][x] = count
            bfs(x-1,y,count+1)
            bfs(x+1,y,count+1)
            bfs(x,y-1,count+1)
            bfs(x,y+1,count+1)
            return True
    return False
max_max = 0
count = 1
for y in range(r):
    for x in range(l):
        bfs(x,y,count)

                        












