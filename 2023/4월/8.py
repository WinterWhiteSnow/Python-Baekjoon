import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/7579
# l,k = wow()
# a_list = [0]+list(wow())
# b_list = [0]+list(wow())
# total = sum(b_list)
# cost = [[0]*(total+1) for _ in range(l+1)]
# # print(cost)
# for index in range(1,l+1):
#     memory,price = a_list[index],b_list[index]
#     for c in range(1,total+1):
#         if c < price:
#             cost[index][c]=cost[index-1][c]
#         else:
#             cost[index][c]=max(cost[index-1][c],cost[index-1][c-price]+memory)
# # # print(cost) 
# for i in range(total+1):
#     if cost[l][i] >= k:
#         print(i)
#         exit()

#https://www.acmicpc.net/problem/25958
# n_list = [0]
# n,k = wow()
# for i in range(1,n+1):
#     num = i
#     number = sum(list(map(int,list(str(num)))))
#     if num%number == 0:
#         n_list.append(num)
# # print(n_list)
# l = len(n_list)-1
# total = [1]*(n+1)
# for index in range(2,l+1):
#     num = n_list[index]
#     for state in range(2,n+1):
#         if num > state:
#             continue
#         total[state]+=total[state-num]
#         total[state]%=k
# print(total[-1])

#https://www.acmicpc.net/problem/9084
# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     k = one()
#     while len(n_list) > 0 and n_list[-1]>k:
#         n_list.pop()
#     l = len(n_list)
#     total = [0]*(k+1)
#     for index in range(l):
#         num = n_list[index]
#         total[num]+=1
#         for state in range(num+1,k+1):
#             total[state]+=total[state-num]
#     print(total[-1])

print(1-(1-0.08)**10)























