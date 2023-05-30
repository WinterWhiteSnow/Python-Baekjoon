import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1342
# a = list(inputing())
# l = len(a)
# if l == 1:
#     print(1)
# else:
#     cnt = 0
#     n_dict = {}
#     for i in range(l):
#         x = a[i]
#         if x not in n_dict:
#             n_dict[x]=1
#         else:
#             n_dict[x]+=1
            
#     def go(ss,str_str,visited,l):
#         global cnt
#         # print("start",str_str,visited)
#         for i in range(l):
#             if visited[i] == False:
#                 visited[i]=True
#                 if len(str_str)== 0:
#                     a = ss[i]
#                     go(ss,a,visited,l)
#                 else:
#                     if str_str[-1] != ss[i]: 
#                         a = str_str+ss[i]
#                         if len(a) != l:
#                             go(ss,a,visited,l)
#                         else:
#                             cnt+=1
#                 visited[i]=False
#     go(a,"",[False]*l,l)
#     for i in n_dict.values():
#         count = 1
#         for a in range(1,i+1):
#             count*=a
#         cnt//=count
#     print(cnt)











