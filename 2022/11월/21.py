import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2246
# r = one()
# list_list = [list(wow()) for _ in range(r)]
# list_list = sorted(list_list,key=lambda x: (x[0],x[1]))
# cnt = 0
# for i in range(r):
#     x,y = list_list[i]
#     check = "yes"
#     for ii in range(r):
#         if i == ii:
#             continue
#         a,b = list_list[ii]
#         if x>=a and y>=b:
#             check ="no"
#             break
#     if check == "yes":
#         cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/13909
# num = one()
# print(int(num**(1/2)))

import heapq
num,r = wow()
n_list = []
for _ in range(r):
    l = one()
    n_list.append(list(wow()))
n_dict = {}
index = 1
while index <= num:
    if len(n_dict) == 0:
        for i in range(len(n_list)):
            n_dict[i]=n_list[i].pop()
    # print(n_dict,index)
    b = min(n_dict.values())
    if index == b:
        index+=1
        for k in n_dict.keys():
            if n_dict[k]==b:
                if len(n_list[k]) >0:
                    n_dict[k]=n_list[k].pop()
                else:
                    n_dict[k]=200001
    else:
        break
        
print("Yes" if index == num+1 else "No")










