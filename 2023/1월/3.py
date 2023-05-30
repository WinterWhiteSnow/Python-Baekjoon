import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2545
# for _ in range(one()):
#     inputing()
#     n_list = list(wow())
#     d = n_list[-1]
#     a,b,c = sorted(n_list[:-1])
#     total = a+b+c-d
#     x = min(total//3,a)
#     total-=x
#     # print(total,x)
#     y = min(total//2,b)
#     total-=y
#     # print(total,y)
#     print(x*y*total)

#https://www.acmicpc.net/problem/9471
# for _ in range(one()):
#     a,m = wow()
#     # n_dict = {}
#     # n_dict[10]=0
#     # n_dict[2]=0
#     # n_dict[5]=0
#     # check = "no"
#     # while b != 0:
#     #     if b%10 == 0:
#     #         if 10 not in n_dict:
#     #             n_dict[10]=0
#     #         n_dict[10]+=1
#     #         b//=10
#     #     elif b%5 == 0:
#     #         if 5 not in n_dict:
#     #             n_dict[5]=0
#     #         n_dict[5]+=1
#     #         b//=5
#     #     elif b%2 == 0:
#     #         if 2 not in n_dict:
#     #             n_dict[2]=0
#     #         n_dict[2]+=1
#     #         b//=2
#     #     else:
#     #         if b == 1:
#     #             check = "yes"
#     #         break
#     #     print(b)
#     x,y = 1,1
#     cnt = 1
#     while True:
#         c = (x+y)%m
#         x,y=y,c
#         if x==y==1:
#             break
#         cnt+=1
#     print(a,cnt)

#https://www.acmicpc.net/problem/2749
# num = one()
# repeat = 1500000
# num%=repeat
# n_list = [0]*(1500001)
# n_list[1]=1
# n_list[2]=1
# for i in range(3,1500001):
#     n_list[i]=(n_list[i-1]+n_list[i-2])%1000000
# print(n_list[num])

import math
r,m = wow()
n_list = [one() for _ in range(r)]
min_min = math.ceil(sum(n_list)/m)
max_max = 10000
while True:
    mid = (min_min+max_max)//2
    # print(min_min,max_max)
    temp = mid
    cnt = 1
    check = "yes"
    for i in n_list:
        if i <= temp:
            temp-=i
        else:
            if mid>=i:
                cnt+=1
                temp = mid
                temp-=i
            else:
                check = "no"
                break
    print(min_min,max_max,mid,cnt,check)
    if cnt == m and check == "yes":
        print(min_min,max_max,mid)
        break
    if check == "no":
        min_min = mid
    else:
        if cnt > m:
            min_min = mid
        else:
            max_max= mid
print(mid)
            









