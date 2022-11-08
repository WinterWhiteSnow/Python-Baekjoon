import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/23056
# num,l = wow()
# n_dict = {}
# while True:
#     a,b = inputing().split()
#     if a==b=="0":
#         break
#     a = int(a)
#     if a not in n_dict:
#         n_dict[a]=[b]
#     else:
#         if len(n_dict[a])<l:
#             n_dict[a]+=[b]
# blue =[]
# white=[]
# for key in n_dict.keys():
#     if key%2:
#         for i in n_dict[key]:  
#             blue.append([key,i])
#     else:
#         for i in n_dict[key]:  
#             white.append([key,i])

# blue.sort(key=lambda x: (len(x[1]),x[1]))
# blue.sort(key=lambda x: x[0])
# white.sort(key=lambda x: (len(x[1]),x[1]))
# white.sort(key=lambda x: x[0])
# for i in blue:
#     print(*i)
# for i in white:
#     print(*i)

#https://www.acmicpc.net/problem/14911
# n_list = list(wow())
# num = one()
# a_list = []
# for a in range(len(n_list)-1):
#     for b in range(a+1,len(n_list)):
#         x=n_list[a]
#         y=n_list[b]
#         if x+y == num:
#             if [x,y] not in a_list:
#                 if [y,x] not in a_list:
#                     if x<=y:
#                         a_list.append([x,y])
#                     else:
#                         a_list.append([y,x])
# a_list.sort(key=lambda x: (x[0],x[1]))
# for i in range(len(a_list)):
#     if i == len(a_list)-1:
#         print(*a_list[i])
#     else:
#         print(*a_list[i],end=" ")
# print(len(a_list))

#https://www.acmicpc.net/problem/14381
# for index in range(1,1+one()):
#     num = one()
#     if num == 0:
#         print(f"Case #{index}: INSOMNIA")
#     else:
#         n_dict= {}
#         cnt = 1
#         while sorted(list(n_dict.keys())) != [str(i) for i in range(10)]:
#             str_str = str(num*cnt)
#             for i in str_str:
#                 n_dict[i]=1
#             cnt+=1
#             # print(n_dict,cnt,sorted(list(n_dict.keys())))
#         cnt-=1
#         print(f"Case #{index}: {cnt*num}")

#https://www.acmicpc.net/problem/1622
# a = "none"
# b = "none"
# n_dict = {}
# for i in sys.stdin.readlines():
#     if a == "none":
#         a = i.strip()
#     else:
#         if b == "none":
#             str_str = []
#             b = i.strip()
#             if len(a) != 0 and len(b) != 0:
#                 if len(a)>len(b):
#                     a,b=b,a
#                 for i in b:
#                     if i not in n_dict:
#                         n_dict[i]=1
#                     else:
#                         n_dict[i]+=1
#                 n_list = []
#                 for i in a:
#                     if i in n_dict:
#                         if n_dict[i]>=1:
#                             str_str+=[i]
#                             n_dict[i]-=1
#                             if n_dict[i] == 0:
#                                 del n_dict[i]
#                 str_str.sort()
#                 print("".join(str_str))
#                 a="none"
#                 b="none"
#                 n_dict={}
#             else:
#                 print("")
#                 a="none"
#                 b="none"
#                 n_dict={}

#https://www.acmicpc.net/problem/5623
# r = one()
# n_list = [list(wow()) for _ in range(r)]
# if r == 2:
#     print(1,n_list[0][1]-1)
# else:
#     x = n_list[0][1]
#     y = n_list[0][2]
#     z = n_list[1][2]
#     num = (x+y-z)//2
#     list_list = n_list[0]
#     list_list[0]=num
#     for i in range(1,len(list_list)):
#         list_list[i]-=num 
#     print(*list_list)               

#https://www.acmicpc.net/problem/8922
# for _ in range(one()):
#     l = one()
#     n_list = list(wow())
#     n_dict = {}
#     check = "no"
#     while True:
#         str_list = list(map(str,n_list))
#         key = "".join(str_list)
#         if key not in n_dict:
#             n_dict[key]=1
#             end = abs(n_list[-1]-n_list[0])
#             list_list = []
#             for i in range(len(n_list)-1):
#                 list_list.append(abs(n_list[i]-n_list[i+1]))
#             list_list.append(end)
#             n_list=list_list     
#             if set(n_list) == {0}:
#                 check="yes"
#                 break          
#         else:
#             break
#         # print(n_dict,check,list_list)
#     print("ZERO" if check == "yes" else "LOOP")











                














