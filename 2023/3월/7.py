import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1010
# total = [0]*31
# total[0]=1 
# total[1]=1
# for _ in range(one()):
#     a,b = wow()
#     a,b = min(a,b),max(a,b)
#     if total[b] == 0:
#         cnt = 1
#         for i in range(2,b+1):
#             cnt*=i
#             total[i]=cnt
#         total[b]=cnt
#     # print(total[b],total[a],total[b-a])
#     count = total[b]//(total[a]*total[b-a])
#     print(count)

#https://www.acmicpc.net/problem/26517
# k = one()
# a,b,c,d = wow()
# if a*k+b == c*k+d:
#     print("Yes",a*k+b)
# else:
#     print("No")

#https://www.acmicpc.net/problem/15739
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# answer = r*(r**2+1)/2
# check = True
# cnt1 = 0
# cnt2 = 0
# n_dict = {}
# for y in range(r):
#     for x in range(r):
#         a = n_list[y][x]
#         if a not in n_dict:
#             n_dict[a]=1
#         else:
#             print("FALSE")
#             exit()
# y_index,x_index=r-1,0
# y,x = 0,0
# # print("Start!!",y_index,x_index)
# for i in range(r):
#     list_list = []
#     for y in range(r):
#         list_list.append(n_list[y][i])
#     if sum(n_list[i]) == answer == sum(list_list):
#         pass
#     else:
#         check = False
#         break
#     cnt2+=n_list[y_index][x_index]
#     cnt1+=n_list[y][x]
#     y+=1
#     x+=1
#     # print(cnt2)
#     # print(y_index,x_index)
#     y_index-=1
#     x_index+=1
# if check:
#     if cnt1==cnt2==answer:
#         pass
#     else:
#         check = False
# print("TRUE" if check else "FALSE")    
















