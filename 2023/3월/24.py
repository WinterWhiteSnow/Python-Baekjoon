import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1270
# for _ in range(one()):
#     n_list = list(wow())
#     n = n_list[0]
#     n_list = n_list[1:]
#     half = n//2+1
#     check = False
#     n_dict = {}
#     # print("start!",half)
#     for i in n_list:
#         if i not in n_dict:
#             n_dict[i]=1
#         else:
#             n_dict[i]+=1
#         # print(i,t[i])
#         if n_dict[i]>=half:
#             print(i)
#             check=True
#             break
    
#     if check == False:
#         print("SYJKGW")

#https://www.acmicpc.net/problem/1515
# from collections import deque
# answer = deque(list(inputing()))
# str_str = ""
# index = 1
# start = 0
# while True:
#     n_list = list(str(index))
#     for i in n_list:
#         if answer[0]==i:
#             answer.popleft()
#             if len(answer)==0:
#                 print(index)
#                 exit()
#     index+=1

#https://www.acmicpc.net/problem/1951
# n = one()
# cnt = 0
# count = 0
# while n != 0:
#     l = len(str(n))
#     cnt+=l*(n-10**(l-1)+1)
#     n = 10**(l-1)-1
# cnt%=1234567
# print(cnt)




    















