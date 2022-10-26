import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/10211
# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     zero_list = [0]*(l+1)
#     max_max = n_list[0]
#     for i in range(l):
#         if i == 0:
#             zero_list[i]=n_list[i]
#         else:
#             zero_list[i]=max(n_list[i]+zero_list[i-1],n_list[i])
#         max_max=max(max_max,zero_list[i])
#     print(max_max)

#https://www.acmicpc.net/problem/11441
# l = one()
# n_list = list(wow())
# zero_list = [0]*l
# for i in range(l):
#     if i == 0:
#         zero_list[i]=n_list[i]
#     else:
#         zero_list[i]=n_list[i]+zero_list[i-1]
# for _ in range(one()):
#     a,b = wow()
#     a,b = a-2,b-1
#     if a < 0:
#         print(zero_list[b])
#     else:
#         print(zero_list[b]-zero_list[a])

#https://www.acmicpc.net/problem/16139
# n_list = list(inputing())
# set_list = set(n_list)
# n_dict = {}
# for i in set_list:
#     n_dict[i] = [0]*(len(n_list))
# for i in range(len(n_list)):
#     n_dict[n_list[i]][i]+=1
# for i in set_list:
#     list_list = n_dict[i]
#     for index in range(1,len(list_list)):
#         list_list[index]=list_list[index]+list_list[index-1]
#     n_dict[i]=list_list

# for _ in range(one()):
#     s,start,end = inputing().split()
#     start,end = int(start),int(end)
#     if s in n_dict:
#         x = end
#         y = start-1
#         if y < 0:
#             print(n_dict[s][end])
#         else:
#             print(n_dict[s][end]-n_dict[s][y])
#     else:
#         print(0)

#https://www.acmicpc.net/problem/1806
# l,count = wow()
# n_list = list(wow())
# zero_list = [0]*l
# min_min = 100000001
# for start in range(l):
#     if start == 0:
#         cnt = 0
#         state = 0
#         for x in range(start,l):
#             state+=n_list[x]
#             cnt+=1
#             if state >= count:
#                 break
#     else:
#         state,cnt = zero_list[start-1]
#         state-=n_list[start-1]
#         cnt-=1
#         if state < count:
#             for x in range(start+cnt,l):
#                 state+=n_list[x]
#                 cnt+=1
#                 if state >= count:
#                     break
#     zero_list[start]=[state,cnt]
#     if state >= count:
#         min_min=min(min_min,cnt)
# print(min_min if min_min != 100000001 else 0) 

#https://www.acmicpc.net/problem/14465
# l,k,r = wow()
# n_list = [1]*(l+1)
# n_list[0]=0
# for _ in range(r):
#     a = one()
#     n_list[a]=0
# zero_list = []
# max_max = 0
# for index in range(1,l+1):
#     if len(zero_list)==0:
#         zero_list.append(sum(n_list[index-1:index-1+k]))
#     else:
#         if index-1+k <= len(n_list):
#             zero_list.append(zero_list[-1]-n_list[index-2]+n_list[index-1+k-1])
#         else:
#             break
#     max_max=max(zero_list[-1],max_max)
# max_max-=k
# if max_max > 0:
#     max_max=0
# print(abs(max_max))

#https://www.acmicpc.net/problem/16507
# r,l,rr = wow()
# n_list = [list(wow()) for _ in range(r)]
# zero_list = []
# for y in range(r):
#     list_list = []
#     for x in range(l):
#         if x==0:
#             list_list.append(n_list[y][x])
#         else:
#             list_list.append(n_list[y][x]+list_list[-1])        
#     zero_list.append(list_list)
# for _ in range(rr):
#     y,x,yy,xx= wow()
#     total = ((xx-x+1)*(yy-y+1))
#     cnt = 0
#     for y_index in range(y-1,yy):
#         if x-2 < 0:
#             cnt+=zero_list[y_index][xx-1]
#         else:
#             cnt+=zero_list[y_index][xx-1]-zero_list[y_index][x-2]
#     print(cnt//total)

#https://www.acmicpc.net/problem/12847
# l,k = wow()
# n_list = list(wow())
# zero_list = [0]*l
# zero_list[0]=sum(n_list[:k])
# max_max = zero_list[0]
# for i in range(1,l-k+1):
#     zero_list[i]=zero_list[i-1]+n_list[i+k-1]-n_list[i-1]
#     max_max=max(zero_list[i],max_max)
# print(max_max)

#https://www.acmicpc.net/problem/15724
# r,l = wow()
# n_list = [list(wow()) for _ in range(r)]
# zero_list = []
# for y in range(r):
#     list_list = []
#     for x in range(l):
#         if x==0:
#             list_list.append(n_list[y][x])
#         else:
#             list_list.append(n_list[y][x]+list_list[-1])        
#     zero_list.append(list_list)
# for _ in range(one()):
#     y,x,yy,xx= wow()
#     cnt = 0
#     for y_index in range(y-1,yy):
#         if x-2 < 0:
#             cnt+=zero_list[y_index][xx-1]
#         else:
#             cnt+=zero_list[y_index][xx-1]-zero_list[y_index][x-2]
#     print(cnt)




