import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/4659
# import string
# jaum_list = list(string.ascii_lowercase)
# moum_list = list("aeiou")
# jaum_list = list(set(jaum_list)-set(moum_list))
# while True:
#     a = inputing()
#     if a == "end":
#         break
    
#     b = list(a)
#     check = "no"
#     for i in moum_list:
#         if i in b:
#             check="yes"
#     if check=="yes":
#         third = 0
#         list_list = []
#         for _ in range(len(b)):
#             if len(list_list) == 0:
#                 list_list.append(b.pop())
#             else:
#                 c = b.pop()
#                 x = list_list[-1]
#                 if x in jaum_list and c in jaum_list:
#                     # print("first")
#                     if x==c:
#                         check="no"
#                         break
#                     else:
#                         if third == 2:
#                             check="no"
#                             break
#                         else:
#                             list_list.append(c)
#                             third=2
#                 elif x in moum_list and c in moum_list:
#                     # print("second")
#                     if x==c=="e" or x==c=="o":
#                         third=2
#                         list_list.append(c)
#                     elif x==c:
#                         check="no"
#                         break
#                     else:
#                         if third == 2:
#                             check="no"
#                             break
#                         else:
#                             list_list.append(c)
#                             third=2
#                 else:
#                     # print("last")
#                     third=0
#                     list_list.append(c)
#             # print(list_list,b,third)
#         if check =="yes":
#             print(f"<{a}> is acceptable.")
#         else:
#             print(f"<{a}> is not acceptable.")
#     else:
#         print(f"<{a}> is not acceptable.")

#https://www.acmicpc.net/problem/20365
# l = one()
# n_list = inputing()
# def check(n_list,a):
#     cnt = 1
#     count = 0
#     for x,y in zip(n_list,a):
#         if x == y:
#             count = 0
#         else:
#             if count == 0:
#                 count+=1
#                 cnt+=1
#             else:
#                 if count>0:
#                     pass
#                 else:
#                     count+=1
#                     cnt+=1
#     return cnt
# print(min(check(n_list,"B"*l),check(n_list,"R"*l)))

#https://www.acmicpc.net/problem/21921
# l,k = wow()
# n_list = list(wow())
# new_list = [sum(n_list[:k])]
# for i in range(l-k):
#     # print(new_list[-1],n_list[i],n_list[i+k])
#     new_list+=[new_list[-1]-n_list[i]+n_list[i+k]]
# max_max = max(new_list)
# if max_max == 0:
#     print("SAD")
# else:
#     print(max_max)
#     print(new_list.count(max_max))











