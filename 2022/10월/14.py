import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/7770
# cnt = 0
# num = one()
# count = 1
# state = 1
# while count <= num:
#     cnt+=1
#     state+=4*cnt
#     count+=state
#     # print(cnt,state,count)    
# print(cnt)

#https://www.acmicpc.net/problem/13015
# num = one()
# gap = []
# state = 0
# while len(gap) != num:
#     if len(gap)==0: 
#         gap.append(state)
#         state+=1
#     else:
#         gap.append(state)
#         state+=2
# gap = gap[::-1]
# index = 0
# str_str = []
# for i in range(num):
#     if i == 0:
#         str_str.append("*"*num+" "*gap[index]+"*"*num)
#     else:
#         if i < num-1:
#             str_str.append(" "*i+"*"+" "*(num-2)+"*"+" "*gap[index]+"*"+" "*(num-2)+"*")
#         else:
#             if i == num-1:
#                 str_str.append(" "*i+"*"+" "*(num-2)+"*"+" "*(num-2)+"*")
#     index+=1
# str_str+=str_str[:num-1][::-1]
# for i in str_str:
#     print(i)

#https://www.acmicpc.net/problem/18511
# import itertools
# n,l = wow()
# n_list = inputing().split()
# a = len(str(n))
# new_list = list(itertools.product(n_list,repeat=a))
# new_list+=list(itertools.product(n_list,repeat=a-1))
# new_list = [int("".join(i)) for i in new_list]
# new_list.sort(reverse=True)
# for i in new_list:
#     if i <= n:
#         print(i)
#         break

#https://www.acmicpc.net/problem/1996
# r = one()
# def bomb(x,y,cnt,repeat):
#     if 0<=x<=r-1 and 0<=y<=r-1:
#         if n_list[y][x] == ".":
#             n_list[y][x]=int(cnt)
#             return
#         if type(n_list[y][x]) == str:
#             if n_list[y][x].isdigit():
#                 if repeat == 0:
#                     n_list[y][x] = "*"
#                     bomb(x-1,y,cnt,repeat+1)
#                     bomb(x-1,y-1,cnt,repeat+1)
#                     bomb(x,y-1,cnt,repeat+1)
#                     bomb(x+1,y-1,cnt,repeat+1)
#                     bomb(x+1,y,cnt,repeat+1)
#                     bomb(x+1,y+1,cnt,repeat+1)
#                     bomb(x,y+1,cnt,repeat+1)
#                     bomb(x-1,y+1,cnt,repeat+1)
#                 else:
#                     return
#         else:
#             answer = int(n_list[y][x])+int(cnt)
#             if answer >= 10:
#                 answer = "M"
#             n_list[y][x]=answer
#             return
    
# n_list = [list(inputing()) for _ in range(r)]
# for yy in range(r):
#     for xx in range(r):
#         if type(n_list[yy][xx]) == str:
#             if n_list[yy][xx] != ".":
#                 bomb(xx,yy,n_list[yy][xx],0)
# for yy in range(r):
#     for xx in range(r):
#         if n_list[yy][xx]==".":
#             n_list[yy][xx]=0
# for i in n_list:
#     print(*i,sep="")

#https://www.acmicpc.net/problem/5671
# for i in sys.stdin.readlines():
#     a,b = map(int,i.split())
#     cnt = 0
#     for i in range(a,b+1):
#         c = list(str(i))
#         d = set(c)
#         if len(c)==len(d):
#             cnt+=1
#     print(cnt)

#https://www.acmicpc.net/problem/17176
# import string
# str_list = list(string.ascii_uppercase)+list(string.ascii_lowercase)
# l = one()
# n_list = list(wow())
# a = list(inputing())
# n_dict = {}
# for i in a:
#     if i not in n_dict:
#         n_dict[i]=1
#     else:
#         n_dict[i]+=1
# new_dict = {}
# for i in n_list:
#     if i == 0:
#         key = " "
#     else:
#         index = i-1
#         key= str_list[index]
#     if key not in new_dict:
#         new_dict[key]=1
#     else:
#         new_dict[key]+=1
# x=sorted(list(n_dict.items()))
# y=sorted(list(new_dict.items()))
# if x==y:
#     print("y")
# else:
#     print("n")

#https://www.acmicpc.net/problem/9037
# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     cnt = 0
#     for i in range(l):
#         if n_list[i]%2:
#             n_list[i]+=1
#     while len(set(n_list)) != 1:
#         new_list = [0]*l
#         cnt+=1
#         for i in range(l):
#             y = (i+1)%l
#             new_list[y]+=n_list[i]//2
#             new_list[i]+=n_list[i]//2
#         for i in range(l):
#             if new_list[i]%2:
#                 new_list[i]+=1
#         # print(new_list)
#         n_list=new_list
#     print(cnt)

#https://www.acmicpc.net/problem/14929
# l = one()
# n_list = list(wow())
# new_list = [0]*l
# new_list[0]=sum(n_list[1:])
# for i in range(1,l):
#     new_list[i]=new_list[i-1]-n_list[i]
# cnt = 0
# for a in range(l-1):
#     cnt+=new_list[a]*n_list[a]
# print(cnt)















