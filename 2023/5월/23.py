import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1821
# n,k= wow()
# n_list = [[1],[1,1]]
# for _ in range(8):
#     m = n_list[-1]
#     a,b = [0]+m,m+[0]
#     c = []
#     for i in range(len(a)):
#         c.append(a[i]+b[i])
#     n_list.append(c)
# list_list = n_list[n-1]

# v = [0]*11
# def check(v,v_list,l,count,index):
#     global n,k
#     if l == n:
#         if count == k:
#             print(*v_list)
#             exit()
#     else:
#         for i in range(1,n+1):
#             if v[i] == 0:
#                 v[i]=1
#                 v_list.append(i)
#                 check(v,v_list,l+1,count+list_list[index]*i,index+1)
#                 v_list.pop()
#                 v[i]=0
                
# check(v,[],0,0,0)





        
    










