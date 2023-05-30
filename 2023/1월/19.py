import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/24061
# l,k = wow()
# n_list = list(wow())
# cnt = 0
# sys.setrecursionlimit(10**6)
# def merge(start,end):
#     global k
#     global cnt
#     # print("state",n_list)
#     list_list = sorted(n_list[start:end])
#     # print("merge_start",list_list,start,end,cnt,k)
#     index = 0
#     for i in range(start,end):
#         n_list[i]=list_list[index]
#         index+=1
#         cnt+=1
#         # print(cnt)
#         # print(*n_list)
#         if cnt == k:
#             print(*n_list)
#             exit()
#         # if cnt == k:
#         #     print(n_list)
    
# def go(start,end):
#     # print("go",start,end)
#     gap = end-start
#     if gap>2:
#         if gap%2:
#             x,y = gap//2+1,gap//2+1
#         else:
#             x,y = gap//2,gap//2
#         go(0+start,x+start)
#         go(x+start,end)
#     if gap > 1:
#         merge(start,end)
        
# if l%2:
#     x,y = n_list[:l//2+1],n_list[l//2+1:]
# else:
#     x,y = n_list[:l//2],n_list[l//2:]
# # print(x,y)
# go(0,len(x))
# go(len(x),l)
# merge(0,l)
# print(-1)


            
















