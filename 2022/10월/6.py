import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/16206
# import heapq
# l,k = wow()
# n_list = list(wow())
# cnt = n_list.count(10)
# n_list = [i for i in n_list if i>10]
# n_list.sort(key=lambda x: (x%10,x))
# while k != 0 and n_list:
#     k-=1
#     a = heapq.heappop(n_list)
#     x,y = a-10,10
#     cnt+=1
#     if x == 10:
#         cnt+=1
#     elif x > 10:
#         heapq.heappush(n_list,x)
#     n_list.sort(key=lambda x: (x%10,x))
#     # print(cnt,k,n_list)   
# print(cnt)     

#색종이 브론즈1
# n_dict = {}
# n_list = [[0]*(1002) for _ in range(1002)]
# for index in range(1,one()+1):
#     a,b,c,d = wow()
#     n_dict[index]=0
#     for y in range(b,b+d):
#         for x in range(a,a+c):
#             if n_list[y][x] == 0:
#                 n_list[y][x]=index
#             else:
#                 n_dict[n_list[y][x]]-=1
#                 n_list[y][x]=index
#             n_dict[index]+=1
# print(*list(n_dict.values()),sep="\n")

#올림픽 실버5
# r,k = wow()
# n_list = []
# for _ in range(r):
#     b = list(wow())
#     if b[0] == k:
#         a = "".join(list(map(str,b[1:])))
#     n_list.append(b[1:])
# n_list.sort(key=lambda x: (x[0],x[1],x[2]),reverse=True)
# n_dict={}
# for i in range(1,r+1):
#     index = "".join(list(map(str,n_list[i-1])))
#     if index not in n_dict:
#         n_dict[index]=i
# print(n_dict[a])

# a,b = wow()
# l = one()
# n_list = list(wow())[::-1]
# cnt = 0
# for i in range(l):
#     cnt+=n_list[i]*(a**i)
# list_list = []
# while cnt != 0:
#     list_list.append(str(cnt%b))
#     cnt//=b
# print(*list_list[::-1])


        
                        
    
    

        
        




