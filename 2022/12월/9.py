import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


#https://www.acmicpc.net/problem/1059
# l = one()
# n_list = sorted(list(wow()))
# # print(n_list)
# num = one()
# start = 0
# end = l-1
# while start<=end:
#     mid = (start+end)//2
#     if n_list[mid]<=num:
#         start=mid+1
#     else:
#         end=mid-1
# # print(start,end,n_list[start],n_list[end])
# if end == -1:
#     end = 0
#     start = 1
#     end = n_list[end]-1
# else:
#     start = n_list[end]+1
#     end = n_list[end+1]-1
# cnt = 0
# for a in range(start,end):
#     for b in range(a+1,end+1):
#         if a<=num<=b:
#             cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/24479
# sys.setrecursionlimit(10**6)
# import heapq
# n,r,start = wow()
# n_dict = {}
# visited = [False]*(n+1)
# list_list = []

# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         heapq.heappush(n_dict[a],b)
#         # n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         heapq.heappush(n_dict[b],a)

# # print(n_dict)
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key])
# def go(number,dict_dict):
#     visited[number]=True
#     list_list.append(number)
#     if number in dict_dict:
#         for i in dict_dict[number]:
#             if visited[i] == False:
#                 go(i,dict_dict)

# go(start,n_dict)
# zero_list = [0]*(n+1)
# for a,b in enumerate(list_list):
#     if zero_list[b] == 0:
#         zero_list[b]=a+1
# print(*zero_list[1:],sep="\n")

#https://www.acmicpc.net/problem/24480
# sys.setrecursionlimit(10**6)
# n_dict = {}
# n,r,start = wow()
# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         n_dict[b]+=[a]
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key],reverse=True)
# check_list = []
# visited = [False]*(n+1)
# def go(number,dict_dict):
#     visited[number]=True
#     check_list.append(number)
#     if number in dict_dict:
#         for i in dict_dict[number]:
#             if visited[i] == False:
#                 go(i,dict_dict)
# go(start,n_dict)
# zero_lsit = [0]*(n+1)
# for a,b in enumerate(check_list):
#     zero_lsit[b]=a+1
# print(*zero_lsit[1:],sep="\n")

#https://www.acmicpc.net/problem/24481
# sys.setrecursionlimit(10**6)
# index = [0]
# n,r,start = wow()
# n_dict = {}
# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         n_dict[b]+=[a]
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key])
# # print(n_dict)
# visited = [False]*(n+1)
# list_list = [-1]*(n+1)
# def go(number,n_dict,cnt):
#     visited[number]=True
#     list_list[number]=cnt
#     if number in n_dict:
#         for i in n_dict[number]:
#             if visited[i] ==False:
#                 go(i,n_dict,cnt+1)
# go(start,n_dict,index[0])
# print(*list_list[1:],sep="\n")    

#https://www.acmicpc.net/problem/24482
# sys.setrecursionlimit(10**6)
# n_dict = {}
# n,r,start = wow()
# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         n_dict[b]+=[a]
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key],reverse=True)
# visited = [False]*(n+1)
# zero_list = [-1]*(n+1)
# def go(number,n_dict,cnt):
#     visited[number]=True
#     zero_list[number]=cnt
#     if number in n_dict:
#         for i in n_dict[number]:
#             if visited[i]==False:
#                 go(i,n_dict,cnt+1)
# go(start,n_dict,0)
# print(*zero_list[1:],sep="\n")

#https://www.acmicpc.net/problem/24483
#https://www.acmicpc.net/problem/24484
# import heapq
# sys.setrecursionlimit(10**6)
# n_dict = {}
# n,r,start = wow()
# visited = [False]*(n+1)
# depth = [-1]*(n+1)
# zero_list = [0]*(n+1)
# check_list = []
# for _ in range(r):
#     a,b = wow()
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         n_dict[a]+=[b]
#     if b not in n_dict:
#         n_dict[b]=[a]
#     else:
#         n_dict[b]+=[a]
# for key in n_dict.keys():
#     n_dict[key]=sorted(n_dict[key],reverse=True)
# def go(number,n_dict,cnt):
#     visited[number]=True
#     depth[number]=cnt
#     check_list.append(number)
#     if number in n_dict:
#         for i in n_dict[number]:
#             if visited[i] == False:
#                 go(i,n_dict,cnt+1)
# go(start,n_dict,0)
# cnt = 0
# for a,b in enumerate(check_list):
#     zero_list[b]=a+1
# for i in range(1,n+1):
#     x,y = depth[i],zero_list[i]
#     cnt+=x*y
# print(cnt)

n,r = wow()
n_dict = {}
for _ in range(r):
    a,b = wow()
    if a not in n_dict:
        n_dict[a]=[b]
    else:
        n_dict[a]+=[b]
    if b not in n_dict:
        n_dict[b]=[a]
    else:
        n_dict[b]+=[a]
print(n_dict)






