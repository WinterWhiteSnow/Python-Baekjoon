import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

import decimal
import math
#https://www.acmicpc.net/problem/3213
# n_list = []
# cnt = 0
# for _ in range(one()):
#     a = inputing()
#     if a == "3/4":
#         if "1/4" in n_list:
#             cnt+=1
#             del n_list[n_list.index("1/4")]
#         else:
#             n_list.append(a)
#     elif a == "1/4":
#         if "3/4" in n_list:
#             cnt+=1
#             del n_list[n_list.index("3/4")]
#         else:
#             n_list.append(a)
#     else:
#         if "1/2" in n_list:
#             cnt+=1
#             del n_list[n_list.index("1/2")]
#         else:
#             n_list.append(a)
# # print(cnt,n_list)
# for _ in range(n_list.count("3/4")):
#     cnt+=1
#     del n_list[n_list.index("3/4")]
# cnt_cnt = decimal.Decimal("0")
# for i in n_list:
#     a,b = i.split("/")
#     cnt_cnt+=(decimal.Decimal(a)/decimal.Decimal(b))
# print(cnt+math.ceil(float(cnt_cnt)))

#https://www.acmicpc.net/problem/14670
# n_dict = {}#효과:이름
# for _ in range(one()):
#     a,b = wow()
#     n_dict[a]=b
# for _ in range(one()):
#     n_list = list(wow())
#     l = n_list[0]
#     n_list = n_list[1:]
#     list_list = []
#     for i in n_list:
#         if i in n_dict:
#             list_list.append(n_dict[i])
#     if len(n_list) == len(list_list):
#         print(*list_list)
#     else:
#         print("YOU DIED")

#https://www.acmicpc.net/problem/17504
# l = one()
# n_list = list(wow())
# x,y = (n_list[-2]*n_list[-1])+1,n_list[-1]
# # print(x,y)
# x,y = y,x
# n_list = n_list[:-2]
# while len(n_list) != 0:
#     num = n_list.pop()
#     x+=num*y
#     x,y = y,x
# print(y-x,y)

#https://www.acmicpc.net/problem/25214
# l = one()
# n_list = list(wow())
# zero_list = []
# min_min = 10**9+1
# for i in n_list:
#     min_min=min(min_min,i)
#     if len(zero_list) == 0:
#         zero_list.append(0)
#     else:
#         gap = i-min_min
#         if gap < 0:
#             gap=0
#         zero_list.append(max(zero_list[-1],gap))
# print(*zero_list)

#https://www.acmicpc.net/problem/2090
# import math
# l = one()
# n_list = list(wow())
# x,y = 0,0
# if l == 1:
#     print(f"{n_list[0]}/1")
# else:
#     while len(n_list) != 0:
#         if x==y==0:
#             a,b = n_list.pop(), n_list.pop()
#             gcd = math.gcd(a,b)
#             a,aa=1,a
#             b,bb=1,b
#             a=a*bb//gcd
#             b=b*aa//gcd
#             x+=a+b
#             y=aa*bb//gcd
#             # print(x,y)
#         else:
#             c = n_list.pop()
#             c,cc = 1,c
#             gcd = math.gcd(cc,y)
#             # print(c,cc,x,y,gcd)
#             x,y,c,cc=x*cc//gcd,y*cc//gcd,c*y//gcd,cc*y//gcd
#             x+=c
#             # print(c,cc,x,y)
#     gcd = math.gcd(y,x)
#     y//=gcd
#     x//=gcd
#     print(f"{y}/{x}")

#https://www.acmicpc.net/problem/23305
# l = one()
# a_list = list(wow())
# b_list = list(wow())
# n_dict={}
# for i in b_list:
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
# for i in a_list:
#     if i in n_dict:
#         n_dict[i]-=1
#         if n_dict[i] == 0:
#             del n_dict[i]
# print(sum(n_dict.values()))
    






