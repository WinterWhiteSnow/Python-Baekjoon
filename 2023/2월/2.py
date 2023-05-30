import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1038
# from collections import deque
# num = one()
# if num == 0:
#     print(0)
# else:
#     n_list = deque()
#     for i in range(1,10):
#         n_list.append(str(i))
#     count =9
#     if num <= count:
#         print(n_list[num-1])
#     else:
#         while count < num:
#             temp_list = deque()
#             while n_list:
#                 a = n_list.popleft()
#                 back = int(a[-1])
#                 for i in range(back):
#                     temp_list.append(a+str(i))
#                     count+=1
#                     if count == num:
#                         print(a+str(i))
#                         exit()
#             if temp_list:
#                 n_list=temp_list
#             else:
#                 break
#         print(-1)


#https://www.acmicpc.net/problem/9742
# def go(state,visited):
#     global k
#     global l
#     global cnt
#     if len(state) == l:
#         cnt+=1
#         if cnt == k:
#             print(*state,sep="")
#             return
#     for i in range(l):
#         if visited[i]==False:
#             visited[i]=True
#             go(state+list_list[i],visited)
#             visited[i]=False
        
        
# def number(list_list,repeat):
#     global k
#     global check
#     if check == "yes":
#         return
#     # print("start_start!!!",list_list,repeat)
#     if k == repeat:
#         if check == "no":
#             print(*list_list,sep="")
#             check="yes"
#         return
#     for back in range(l-1,0,-1):
#         if list_list[back-1] < list_list[back]:
#             for front in range(l-1,0,-1):
#                 if list_list[back-1]<list_list[front]:
#                     list_list[back-1],list_list[front]=list_list[front],list_list[back-1]
#                     list_list = list_list[:back]+sorted(list_list[back:])
#                     number(list_list,repeat+1)
#     return                 
# def str_str(list_list,repeat):
#     global k
#     global check
#     # print("Start!!!",list_list,repeat)
#     if check == "yes":
#         return
#     if k == repeat:
#         if check == "no":
#             print(*list_list,sep="")
#             check = "yes"
#         return
#     for back in range(l-1,0,-1):
#         if ord(list_list[back-1]) < ord(list_list[back]):
#             for front in range(l-1,0,-1):
#                 if ord(list_list[back-1])<ord(list_list[front]):
#                     list_list[back-1],list_list[front]=list_list[front],list_list[back-1]
#                     list_list = list_list[:back]+sorted(list_list[back:])
#                     number(list_list,repeat+1)
#     return
    
# from collections import deque
# from itertools import permutations
# n_list = deque()  
# for i in sys.stdin.readlines():
#     i = i.rstrip()
#     a,b = i.split()
#     start = a
#     b = int(b)
#     if a[0].isdigit():
#         type = "num"
#     else:
#         type = "str"
#     a = list(a)
#     # if type == "num":
#     #     a = list(map(int,a))
#     n_list.append((a,b,type,start))
# while n_list:
#     list_list,k,type,start = n_list.popleft()
#     l = len(list_list)
#     check = "no"
#     max_max = 1
#     for i in range(1,l+1):
#         max_max*=i
#     # print(k,max_max)
#     cnt = 0
#     print(start,k,"=",end=" ")
#     vistied = [False]*l
#     if max_max >=k:
#         go("",vistied)
#     else:
#         print("No permutation")
    
#https://www.acmicpc.net/problem/10597    
# n = inputing()  
# str_str = ""
# ind = 1
# while len(str_str) != len(n):
#     str_str+=str(ind)
#     ind+=1
# l = len(n)
# visited = [False]*ind
# check = "no"
# def go(list_list,index,n_list):
#     global l
#     global ind
#     global check
#     str_str = ""
#     if len(n_list) == ind-1:
#         if check == "no":
#             print(*n_list)
#             check="yes"
#             return
    
#     # print("start",list_list,index,n_list)
#     if index < l:
#         for i in range(index,l):
#             str_str+=list_list[i]
#             if int(str_str) < ind:
#                 if int(str_str) != False:
#                     if visited[int(str_str)]==False:
#                         visited[int(str_str)]=True
#                         n_list.append(str_str)
#                         go(list_list,i+1,n_list)
#                         visited[int(str_str)]=False
#                         n_list.pop()
# go(n,0,[])

















