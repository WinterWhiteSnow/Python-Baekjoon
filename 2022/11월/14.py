import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2346 
# from collections import deque
# l = one()
# n_list = list(wow())
# for i in range(l):
#     n_list[i]=[n_list[i],i+1]
# n_list = deque(n_list)
# index_list = []
# for _ in range(l):
#     key = n_list[0]
#     index_list.append(key)
#     rotate = key[0]
#     if rotate > 0:
#         rotate-=1
#     del n_list[n_list.index(index_list[-1])]
#     n_list.rotate(-rotate)
# index_list = [i[1] for i in index_list]
# print(*index_list)

#https://www.acmicpc.net/problem/17175
# num = one()
# n_list = [1,1]
# if num < 2:
#     print(1)
# else:
#     while len(n_list)<=num:
#         n_list.append((n_list[-1]+n_list[-2])%1000000007)
#     print((sum(n_list[-3:])%1000000007)-1)

#https://www.acmicpc.net/problem/14235
# import heapq
# h = []
# for _ in range(one()):
#     a = list(wow())
#     if a[0] == 0:
#         if len(h) > 0:
#             print(-heapq.heappop(h))
#         else:
#             print(-1)
#     else:
#         a = a[1:]
#         for i in a:
#             heapq.heappush(h,-i)

#https://www.acmicpc.net/problem/14246
# l = one()
# n_list = list(wow())
# k = one()
# count = 0
# for x in range(l-1):
#     cnt = n_list[x]
#     for y in range(x+1,l):
#         if cnt < k:
#             cnt+=n_list[y]
#             if cnt > k:
#                 # print("first",x,y)
#                 count+=l-y
#                 break
#         else:
#             # print("second",x,y)
#             count+=l-y
#             break
# print(count)

#https://www.acmicpc.net/problem/12933
a = list(inputing())
str_str = "quack"
count = 0
while len(a)>=5:
    index = 0
    list_list = []
    check = "no"
    temp_list = []
    for ind in range(len(a)):
        key= str_str[index]
        if key == a[ind]:
            index+=1
            temp_list.append(ind)
            if index == len(str_str):
                check ="yes"
                index=0
                list_list.extend(temp_list)
                temp_list=[]
    if check == "yes":
        count+=1
    str_list = []
    for index in range(len(a)):
        if index not in list_list:
            str_list.append(a[index])
    if a != str_list:
        a = str_list
    else:
        break
if len(a) == 0:
    print(count)
else:
    print(-1)


        



















