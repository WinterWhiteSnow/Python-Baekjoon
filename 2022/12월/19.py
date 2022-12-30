import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/2447
# r = one()
# n_list = [list("*"*r) for _ in range(r)]
# def go(n,x,y):
#     num = n//3
#     if num == 0:
#         return
#     # print("Start",num,x,y)
#     for a in range(3):
#         for b in range(3):
#             if a==b==1:
#                 for i in range(num):
#                     n_list[y+num*b+i][x+num*a:x+num*a+num]=" "*num
#                     # print(y+num*b+i,x+num*a,x+num*a+num,num)
#             go(num,x+num*a,y+num*b)
# go(r,0,0)
# for i in n_list:
#     print(*i,sep="")    

#https://www.acmicpc.net/problem/2630
# n = one()
# white = [0]
# blue = [0]
# n_list = [list(wow()) for _ in range(n)]
# count = 0
# s = "none"
# check ="yes"
# for i in n_list:
#     set_list = list(set(i))
#     if len(set_list) == 1:
#         if s == "none":
#             count+=1
#             s = set_list[0]
#         else:
#             if set_list[0] != s:
#                 check = "no"
#                 break
#             else:
#                 count+=1
#     else:
#         check ="no"
#         break
# if check == "yes":
#     if s == 1:
#         blue[0]+=1
#     else:
#         white[0]+=1
#     print(white[0])
#     print(blue[0])
# else:
#     def go(n,x,y):
#         num = n//2
#         if num == 0:
#             return
#         # print("Start",num,x,y)
#         for a in range(2):
#             for b in range(2):
#                 cnt = 0
#                 state = "none"
#                 for i in range(num):
#                     set_list = list(set(n_list[y+num*a+i][x+num*b:x+num*b+num]))
#                     # print("wow",n_list[y+num*a+i][x+num*b:x+num*b+num])
#                     # print(y+num*a+i,x+num*b,x+num*b+num)
#                     if len(set_list)== 1:
#                         if state == "none":
#                             state = set_list[0]
#                             cnt+=1
#                         else:
#                             if state != set_list[0]:
#                                 cnt=0
#                                 break
#                             else:
#                                 cnt+=1
#                     else:
#                         break
#                 # print(a,b,cnt,num,state)
#                 if cnt == num:
#                     if state == 1:
#                         blue[0]+=1
#                     else:
#                         white[0]+=1
#                 else:
#                     # print("try")
#                     # print(a,b,cnt,num,state)
#                     go(num,x+num*b,y+num*a)
#     go(n,0,0)
#     print(white[0])
#     print(blue[0])      
# 4
# 1 1 0 0
# 1 1 0 0
# 0 0 1 0
# 0 0 0 1
# 4
# 1 1 1 0
# 1 1 1 0
# 1 1 1 0
# 1 1 1 0

#https://www.acmicpc.net/problem/1780
# n = one()
# zero_zero= [0]
# one_one = [0]
# minus_minus = [0]
# n_list = [list(wow()) for _ in range(n)]
# count = 0
# s = "none"
# check ="yes"
# for i in n_list:
#     set_list = list(set(i))
#     if len(set_list) == 1:
#         if s == "none":
#             count+=1
#             s = set_list[0]
#         else:
#             if set_list[0] != s:
#                 check = "no"
#                 break
#             else:
#                 count+=1
#     else:
#         check ="no"
#         break
# if check == "yes":
#     if s == 1:
#         one_one[0]+=1
#     elif s == -1:
#         minus_minus[0]+=1
#     else:
#         zero_zero[0]+=1
#     print(minus_minus[0])
#     print(zero_zero[0])
#     print(one_one[0])
# else:
#     def go(n,x,y):
#         num = n//3
#         if num == 0:
#             return
#         # print("Start",num,x,y)
#         for a in range(3):
#             for b in range(3):
#                 cnt = 0
#                 state = "none"
#                 for i in range(num):
#                     set_list = list(set(n_list[y+num*a+i][x+num*b:x+num*b+num]))
#                     # print("wow",n_list[y+num*a+i][x+num*b:x+num*b+num])
#                     # print(y+num*a+i,x+num*b,x+num*b+num)
#                     if len(set_list)== 1:
#                         if state == "none":
#                             state = set_list[0]
#                             cnt+=1
#                         else:
#                             if state != set_list[0]:
#                                 cnt=0
#                                 break
#                             else:
#                                 cnt+=1
#                     else:
#                         break
#                 # print(a,b,cnt,num,state)
#                 if cnt == num:
#                     if state == 1:
#                         one_one[0]+=1
#                     elif state == 0:
#                         zero_zero[0]+=1
#                     else:
#                         minus_minus[0]+=1
#                 else:
#                     # print("try")
#                     # print(a,b,cnt,num,state)
#                     go(num,x+num*b,y+num*a)
#     go(n,0,0)
#     print(minus_minus[0])
#     print(zero_zero[0])
#     print(one_one[0])

str_str = [0]
l = one()
while len(str_str)<l:
    list_list = list(str_str)
    list_list =  [not i for i in list_list]
    for i in list_list:
        str_str+=[i]
print(1 if str_str[l-1] ==True else 0)











