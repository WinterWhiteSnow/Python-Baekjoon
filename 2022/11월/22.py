import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2057
# num = one()
# if num == 0:
#     print("NO")
# else:
#     n_list = [1]
#     index = 1
#     while n_list[-1]*index <= num:
#         n_list.append(n_list[-1]*index)
#         index+=1
#     n_list=n_list[::-1]
#     for i in n_list:
#         if num>=i:
#             num-=i
#     print("YES" if num == 0 else "NO")

#https://www.acmicpc.net/problem/14492
# r = one()
# a_list = [list(wow()) for _ in range(r)]
# b_list = [list(wow()) for _ in range(r)]
# cnt = 0
# for y in range(r):
#     for x in range(r):
#         state = "none"
#         for index in range(r):
#             a,b = a_list[y][index],b_list[index][x]
#             if state == "none":
#                 state = a&b
#             else:
#                 state|=(a&b)
#         cnt+=state
# print(cnt)

#https://www.acmicpc.net/problem/5534
# r = one()
# n_list = inputing()
# cnt = 0
# for _ in range(r):
#     a = list(inputing())
#     check = "no"
#     for i in range(len(a)-len(n_list)+1):
#         if a[i] == n_list[0]:
#             gap = 1
#             index = i
#             while i+(len(n_list)-1)*gap <= len(a)-1:
#                 # print("start",gap)
#                 str_str = a[i]
#                 list_list = []
#                 for _ in range(len(n_list)-1):
#                     index+=gap
#                     str_str+=a[index]
#                     list_list.append(index)
#                 # print("str",str_str,i,gap,index)
#                 if str_str == n_list:
#                     # print(list_list)
#                     check ="yes"
#                     break
#                 else:
#                     gap+=1
#                     index = i
#             if check == "yes":
#                 break
#         if check =="yes":
#             break
#     if check == "yes":
#         cnt+=1
# print(cnt)
                
# l = one()
# n_list = inputing()
# sk = []
# lr = []
# cnt = 0
# for i in n_list:
#     if i.isdigit():
#         cnt+=1
#     else:
#         if i == "S":
#             sk.append("S")
#         elif i == "L":
#             lr.append("L")
#         else:
#             if i == "K":
#                 if len(sk)>0:
#                     cnt+=1
#                     sk.pop()
#                 else:
#                     break
#             else:
#                 if len(lr)>0:
#                     cnt+=1
#                     lr.pop()
#                 else:
#                     break
# print(cnt)

#https://www.acmicpc.net/problem/10431
# for _ in range(one()):
#     n_list = list(wow())
#     num = n_list[0]
#     n_list=n_list[1:]
#     max_max = n_list[0]
#     l = len(n_list)
#     a_list = sorted(n_list)
#     cnt = 0
#     index = 0
#     while index < l:
#         i = n_list.index(a_list[index])
#         cnt+=abs(index-i)
#         del n_list[i]
#         n_list.insert(index,a_list[index])
#         index+=1
#     print(num,cnt)

#https://www.acmicpc.net/problem/6463
# n_list = [0]*(10001)
# n_list[1]=1
# for i in range(2,10001):
#     num = i
#     while True:
#         if num%10==0:
#             num//=10
#         else:
#             break
#     cnt=n_list[i-1]*num
#     while True:
#         if cnt%10==0:
#             cnt//=10
#         else:
#             break
#     n_list[i]=cnt
# for i in sys.stdin.readlines():
#     num = int(i.strip())
#     print(str(num).rjust(5),"->",str(n_list[num])[-1])













