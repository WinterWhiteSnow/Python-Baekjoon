import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/1057
# n,a,b = wow()
# n_list = [i for i in range(1,n+1)]
# cnt = 0
# while len(n_list) != 1:
#     new_list = []
#     l = len(n_list)
#     cnt+=1
#     wait = "none"
#     if l%2:
#         wait = n_list.pop()
#         l-=1
#     for index in range(0,l,2):
#         x = n_list[index]
#         y = n_list[index+1]
#         if sorted([x,y]) == sorted([a,b]):
#             print(cnt)
#             exit()
#         else:
#             if x in [a,b]:
#                 new_list.append(x)
#             elif y in [a,b]:
#                 new_list.append(y)
#             else:
#                 new_list.append(x)
#     if wait != "none":
#         new_list.append(wait)
#     n_list=new_list

# r,l = wow()
# max_l = min(r,l)
# cnt = 0
# n_list = [list(inputing()) for _ in range(r)]
# while max_l != 0:
#     for y in range(0,r-max_l+1):
#         for x in range(0,l-max_l+1):
#             a,b,c,d = n_list[y][x],n_list[y+max_l-1][x],n_list[y+max_l-1][x+max_l-1],n_list[y][x+max_l-1]
#             if a==b==c==d:
#                 cnt = max(cnt,((y+max_l-y)**2))
#     max_l-=1
# print(cnt)

# n_dict = {}
# for _ in range(one()):
#     num = inputing()[::-1]
#     l = len(num)
#     for i in range(l):
#         c = num[i]
#         if c not in n_dict:
#             n_dict[c]=10**i
#         else:
#             n_dict[c]+=10**i
# list_list = [b for a,b in sorted(list(n_dict.items()),key = lambda x: x[1],reverse=True)]
# cnt = 0
# number = 9
# for i in list_list:
#     cnt+=i*number
#     number-=1
# print(cnt)

#1744
# minus_list = []
# plus_list = []
# for _ in range(one()):
#     num = one()
#     if num <=0:
#         minus_list.append(num)
#     else:
#         plus_list.append(num)
# minus_list.sort()
# plus_list.sort(reverse=True)
# minus_l = len(minus_list)
# plus_l = len(plus_list)
# cnt = 0
# if minus_l%2:
#     minus_l-=1
#     cnt+=minus_list.pop()
# if plus_l%2:
#     plus_l-=1
#     cnt+=plus_list.pop()

# def cal(list_list,l):
#     count = 0
#     for i in range(0,l,2):
#         a,b = list_list[i],list_list[i+1]
#         count+=max(a+b,a*b)
#     return count
# cnt+=cal(plus_list,plus_l)+cal(minus_list,minus_l)
# print(cnt)

# https://www.acmicpc.net/problem/1132
# n_dict = {}
# first_list = []
# for _ in range(one()):
#     num = inputing()
#     first_list.append(num[0])
#     num=num[::-1]
#     l = len(num)
#     for i in range(l):
#         a = num[i]
#         if a not in n_dict:
#             n_dict[a]=10**i
#         else:
#             n_dict[a]+=10**i
# list_list = list(n_dict.items())
# f_list = []
# n_list = []
# for i in range(len(list_list)):
#     a,b = list_list[i]
#     if a in first_list:
#         c=1
#         f_list.append([a,b,c])
#     else:
#         c=0
#         n_list.append([a,b,c])
# f_list.sort(key=lambda x: x[1],reverse=True)
# n_list.sort(key=lambda x: x[1])
# if len(list_list)==10:
#     if n_list:
#         for i in range(len(f_list)):
#             score = f_list[i][1]
#             start = 0
#             end = len(n_list)-1
#             # print("end",end)
#             while start<=end:
#                 mid = (start+end)//2
#                 mid_score = n_list[mid][1]
#                 if score > mid_score:
#                     start = mid+1
#                 else:
#                     end=mid-1
#             start = min(len(n_list)-1,start)
#             if n_list[start][1]<score:
#                 n_list.insert(start+1,f_list[i])
#             else:
#                 if start == 0:
#                     start +=1
#                 n_list.insert(start,f_list[i])
#         n_list = n_list[::-1]
#         # print(n_list)
#         num = 9
#         cnt = 0
#         for i in n_list:
#             # print(i)
#             cnt+=i[1]*num
#             num-=1
#         print(cnt)
#     else:
#         cnt = 0
#         num = 9
#         for i in f_list:
#             cnt+=i[1]*num
#             num-=1
#         print(cnt)
# else:
#     # print("wow!")
#     list_list = sorted(list_list,key=lambda x:x[1],reverse=True)
#     print(list_list)
#     cnt = 0
#     num = 9
#     for i in list_list:
#         cnt+=i[1]*num
#         num-=1
#     print(cnt)









