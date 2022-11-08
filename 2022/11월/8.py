import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10451
# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     n_dict = {}
#     num_list = sorted(n_list)
#     visited = [False]*(l+1)
#     for a,b in zip(n_list,num_list):
#         if a not in n_dict:
#             n_dict[a]=[b]
#         else:
#             if b not in n_dict[a]:
#                 n_dict[a]+=[b]
#         if b not in n_dict:
#             n_dict[b]=[a]
#         else:
#             if a not in n_dict[b]:
#                 n_dict[b]+=[a]
#     cnt = 0
#     def dfs(list_list,key,visited):
#         visited[key]=True
#         for i in list_list:
#             if not visited[i]:
#                 dfs(n_dict[i],i,visited)
#     for key in range(1,l+1):
#         if visited[key] == False:
#             cnt+=1
#             dfs(n_dict[key],key,visited)
#     print(cnt)

#https://www.acmicpc.net/problem/18917
# three = 0
# four = 0
# for _ in range(one()):
#     n = inputing().split()
#     if len(n) ==2:
#         if n[0] == "1":
#             three+=int(n[1])
#             four^=int(n[1])
#         else:
#             three-=int(n[1])
#             four^=int(n[1])
#     else:
#         if n[0] == "3":
#             print(three)
#         else:
#             print(four)

#https://www.acmicpc.net/problem/2312
# n_dict = {}
# for i in range(2,100000+1):
#     if i not in n_dict:
#         for a in range(i,100000+1,i):
#             n_dict[a]=0
#         n_dict[i]=1
# list_list = [a for a,b in n_dict.items() if b == 1]
# list_list.sort()
# for _ in range(one()):
#     num = one()
#     number = num
#     start =0
#     end=len(list_list)-1
#     while start<=end:
#         mid = (start+end)//2
#         if list_list[mid]>=num:
#             end=mid-1
#         else:
#             start=mid+1
#     n_dict = {}
#     cnt = 1
#     for index in list_list[:start+1]:
#         if num != 0:
#             if num%index == 0:
#                 n_dict[index]=0
#                 while num != 0:
#                     if num%index==0:
#                         num//=index
#                         cnt*=index
#                         n_dict[index]+=1
#                     else:
#                         break
#     if cnt == number:
#         new_list = list(n_dict.items())
#         new_list.sort(key=lambda x: x[0])
#         for a,b in new_list:
#             print(a,b)

#https://www.acmicpc.net/problem/16165
# r,rr = wow()
# n_dict = {}
# for _ in range(r):
#     a = inputing()
#     r = one()
#     for _ in range(r):
#         c = inputing()
#         if a not in n_dict:
#             n_dict[a]=[c]
#         else:
#             n_dict[a]+=[c]
#         n_dict[c]=a
#     n_dict[a] = sorted(n_dict[a])
# for _ in range(rr):
#     a = inputing()
#     b = one()
#     if b == 0:
#         for i in n_dict[a]:
#             print(i)
#     else:
#         print(n_dict[a])

#https://www.acmicpc.net/problem/17829
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# while r != 2:
#     new_list = []
#     for y in range(0,r,2):
#         n_dict = {}
#         for y_index in range(y,y+2):
#             for x in range(0,r,2):
#                 # print(n_list[y_index][x:x+2])
#                 if x not in n_dict:
#                     n_dict[x]=n_list[y_index][x:x+2]
#                 else:
#                     n_dict[x]+=n_list[y_index][x:x+2]
#         list_list = list(map(sorted,list(n_dict.values())))
#         list_list = [a[-2] for a in list_list]
#         # print(list_list)
#         new_list.append(list_list)
#     r = r//2
#     n_list = new_list
# end_list = []
# for i in n_list:
#     end_list.extend(i)
# end_list.sort(reverse=True)
# print(end_list[1])

#https://www.acmicpc.net/problem/21919
# n_dict = {}
# for i in range(2,1000001):
#     if i not in n_dict:
#         for a in range(i,1000001,i):
#             n_dict[a]=0
#         n_dict[i]=1
# list_list = [a for a,b in n_dict.items() if b == 1]
# list_list.sort()
# l = one()
# n_list = list(wow())
# cnt = 1
# for i in n_list:
#     if i in list_list:
#         if cnt%i != 0:
#             cnt*=i
# print(cnt if cnt != 1 else -1)

#https://www.acmicpc.net/problem/16471
# l = one()
# n_list = sorted(list(wow()),reverse=True)
# a_list = sorted(list(wow()))
# cnt = 0
# for i in a_list:
#     if i > n_list[-1]:
#         n_list.pop()
#         cnt+=1
# number = (l+1)//2
# print("YES" if cnt>=number else "NO")

#https://www.acmicpc.net/problem/3182
# n_dict = {}
# max_max = 0
# state = "none"
# r = one()
# for i in range(1,1+r):
#     num = one()
#     n_dict[i]=[num]
# def go(list_list,num,visited):
#     visited[num]=True
#     cnt[0]+=1
#     for i in list_list:
#         if not visited[i]:
#             go(n_dict[i],i,visited)
# for key in range(1,r+1):
#     visited =[False]*(r+1)
#     cnt = [0]
#     go(n_dict[key],key,visited)
#     if state == "none":
#         state = key
#         max_max = cnt[0]
#     else:
#         if cnt[0] > max_max:
#             max_max=cnt[0]
#             state = key
#         else:
#             if cnt[0] == max_max:
#                 state = min(state,key)
# print(state)

import datetime

print(datetime.date(year=2022,month=11,day=8)-datetime.date(year=2022,month=6,day=9))
print(1000/152)




