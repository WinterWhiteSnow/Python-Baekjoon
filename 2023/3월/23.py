import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1464
# import string
# index = 0
# n_dict= {}
# for i in string.ascii_uppercase:
#     n_dict[i]=index
#     index+=1
# n_list = list(inputing())
# state = n_dict[n_list[0]]
# str_list = [n_list[0]]
# for i in n_list[1:]:
#     index = n_dict[i]
#     if index >state:
#         str_list = str_list[::-1]
#         str_list.append(i)
#         str_list= str_list[::-1]
#     else:
#         str_list.append(i)
#     state = n_dict[str_list[-1]]
#     # print(str_list,str_list[-1],n_dict[str_list[-1]],state)
# print("".join(str_list[::-1]))
        
#https://www.acmicpc.net/problem/15738        
# l,k,r = wow()
# reverse_k = l-k+1
# n_list = list(wow())
# for _ in range(r):
#     # print("start!",k,reverse_k)
#     index = one()
#     if index >0:
#         if k>index:
#             pass
#         else:
#             k = index-k+1
#             reverse_k=l-k+1
#     else:
#         if reverse_k>abs(index):
#             pass
#         else:
#             reverse_k=abs(index)-reverse_k+1
#             k = l-reverse_k+1
#     # print("end",k,reverse_k)      
# print(k)

from collections import deque
l,k= wow()
k = l-k
n_list = list(map(int,list(inputing())))
print(n_list)
zero_list = [0]*l
for end in range(l):
    for start in range(end):
        num = n_list[end]
        if n_list[start]<num:
            zero_list[end]= max(zero_list[end],zero_list[start]+1)
print(zero_list)


        











