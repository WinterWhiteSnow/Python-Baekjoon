import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/22857
# l,k = wow()
# n_list = list(wow())
# index_list = []
# for i in range(l):
#     if n_list[i]%2 == 0:
#         index_list.append(i)
# gap = []
# for i in range(1,len(index_list)):
#     gap.append(index_list[i]-index_list[i-1]-1)
# start = 0
# end = 0
# l = len(gap)
# max_max = 0
# count = 1
# total = 0
# while start<l:
#     # print("start!",start)
#     while end<l:
#         if total+gap[end]<=k:
#             total+=gap[end]
#             count+=1
#             end+=1
#         else:
#             # print("wa!",count,max_max)
#             max_max = max(max_max,count)
#             break  
#     # print("end",gap[start:end+1],count,max_max)  
#     max_max = max(max_max,count)
#     count-=1
#     total-=gap[start]        
#     start+=1
# if len(index_list) != 0:
#     max_max = max(max_max,1)
# print(max_max)













