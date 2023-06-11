import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1411
# import string
# str_str = list(string.ascii_lowercase)
# r = one()
# n_list = [list(inputing()) for _ in range(r)]
# cnt = 0
# for start in range(r-1):
#     for end in range(start+1,r):
#         visit = [0]*len(str_str)
#         a,b = n_list[start],n_list[end]
#         n_dict = {}
#         state = True
#         for i in range(len(a)):
#             x,y = a[i],b[i]
#             if x not in n_dict:
#                 if visit[str_str.index(y)]==0:
#                     n_dict[x]=y
#                     visit[str_str.index(y)]=1
#                 else:
#                     state = False
#                     break
#             else:
#                 if n_dict[x] ==y:
#                     continue
#                 state = False
#                 break
#         if state == True:
#             for i in range(len(a)):
#                 a[i]=n_dict[a[i]]
#             if a==b:
#                 cnt+=1
# print(cnt)

      


















