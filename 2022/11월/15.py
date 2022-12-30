import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2757
# import string
# str_str = list(string.ascii_uppercase)
# while True:
#     a = inputing()
#     if a == "R0C0":
#         break
#     r_index = a.index("R")
#     c_index = a.index("C")
#     r_num = a[r_index+1:c_index] #그대로
#     c_num = a[c_index+1:]
#     c_num = int(c_num)
#     list_list = []
#     while c_num != 0:
#         list_list.append(c_num%26)
#         c_num//=26
#     list_list = list_list[::-1]
#     # print(list_list)
#     while 0 in list_list:
#         # print("Start",list_list)
#         for i in range(1,len(list_list)):
#             # print(i)
#             number = list_list[i]
#             if number == 0:
#                 list_list[i-1]-=1
#                 list_list[i]+=26
#         if list_list[0] == 0:
#             list_list=list_list[1:]
#     str_list = ""
#     for i in list_list:
#         if i != 0:
#             str_list+=str_str[i-1]
#     print(str_list+r_num)

#https://www.acmicpc.net/problem/25418
# a,b = wow()
# n_list = [0]*(b+1)
# n_list[a]=1
# for x in range(a+1,b+1):
#     if x >= a*2:
#         if x%2 == 0:
#             n_list[x]=min(n_list[x//2]+1,n_list[x-1]+1)
#         else:
#             n_list[x]=n_list[x-1]+1
#     else:
#         n_list[x]=n_list[x-1]+1
# print(n_list[b]-1)

#https://www.acmicpc.net/problem/2986
# n = one()
# number = n
# index = n-1
# if index == 0:
#     print(index)
# else:
#     index = int(n**(1/2))
#     n_list = []
#     for i in range(2,index+1):
#         while True:
#             if n%i == 0:
#                 n_list.append(i)
#                 n//=i
#             else:
#                 break
#     if n>=2:
#         n_list.append(n)
#     n_list.sort(reverse=True)
#     # print(n_list)
#     cnt = 1
#     n_list.pop()
#     for i in n_list:
#         cnt*=i
#     print(number-cnt)
        

    



























