import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/5555
# a = inputing()
# cnt = 0
# for _ in range(one()):
#     b = inputing()
#     b+=b
#     if a in b:
#         cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/24039
# n = one()
# n_dict = {}
# for i in range(2,200):
#     if i not in n_dict:
#         for ii in range(i,200,i):
#             n_dict[ii]=0
#         n_dict[i]=1
# list_list=[a for a,b in n_dict.items() if b == 1]
# list_list.sort()
# # print(list_list)
# for i in range(len(list_list)-1):
#     a,b = list_list[i],list_list[i+1]
#     if a*b>n:
#         print(a*b)
#         break

#https://www.acmicpc.net/problem/1531
# n_list = [[0]*101 for _ in range(101)]
# a,b = wow()
# total = 100*100
# for _ in range(a):
#     x,y,xx,yy=wow()
#     for y_index in range(y,yy+1):
#         for x_index in range(x,xx+1):
#             check = n_list[y_index][x_index]
#             if check<=b:
#                 check+=1
#                 if check > b:
#                     total-=1
#             n_list[y_index][x_index]=check
# print(100*100-total)

#https://www.acmicpc.net/problem/9324
# for _ in range(one()):
#     a = inputing()
#     set_a = set(list(a))
#     state ="yes"
#     result = "yes"
#     for i in set_a:
#         cnt = 0
#         state = "none"
#         for ii in range(len(a)):
#             if a[ii] == i:
#                 cnt+=1
#                 if cnt == 3:
#                     state = ii
#                 if cnt == 4:
#                     if ii-1 == state:
#                         state = "none"
#                         cnt = 0
#                     else:
#                         result = "no"
#                         break
#         if cnt == 3:
#             result = "no"
#         if result == "no":
#             break
#     print("OK" if result == "yes" else "FAKE")

#https://www.acmicpc.net/problem/12871
# import math
# a = inputing()
# b = inputing()
# if a == b:
#     print(1)
# else:
#     max_l = len(a)*len(b)//math.gcd(len(a),len(b))
#     a = a*(max_l//len(a))
#     b = b*(max_l//len(b))
#     if a==b:
#         print(1)
#     else:
#         print(0)





