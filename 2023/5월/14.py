import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/17271
# from itertools import permutations,product
# n,m = wow()
# n_list = [1,m]
# for i in range(2,n+1):
#     temp_list = []
#     for k in range(1,i+1):
#         new_list = list(product(n_list,repeat=k))
#         new_list = [index for index in new_list if sum(index) == i]
#         temp_list.extend(new_list)
#     print(i,len(temp_list))

# n,m = wow()
# n_list = [0]*(n+1)
# # print(n_list)
# for i in range(1,min(m+1,n+1)):
#     # print("Start",i)
#     if i != m:
#         n_list[i]=1
#     else:
#         n_list[i]=2
# for k in range(m+1,n+1):
#     n_list[k]=n_list[k-1]+n_list[k-m]
#     n_list[k]%=1000000007
# print(n_list[-1])

# n,k = map(int,(input().split()))
# total = [0]*(n+1)
# for i in range(1,min(k+1,n+1)):
#     if i != k:
#         total[i]=1
#     else:
#         total[i]=2

# for i in range(k+1,n+1):
#     if i >k:
#         total[i]=total[i-1]+total[i-k]
 
#         total[i]%=1000000007

        
        
# print(total[-1])
















