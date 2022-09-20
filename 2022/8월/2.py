import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#오늘 총 38문제

# while True:
#     a = inputing()
#     if a == "#":
#         break
    
#     right = "qwertasdfgzxcvb"
#     left = "yuiophjklnm"
#     state = "none"
#     cnt = 0
#     for i in range(len(a)):
#         if i == 0:
#             if a[i] in right:
#                 state = "right"
#             else:
#                 state = "left"
#         else:
#             if state == "right":
#                 if a[i] in right:
#                     pass
#                 else:
#                     cnt+=1
#                     state = "left"
#             else:
#                 if a[i] in left:
#                     pass
#                 else:
#                     cnt+=1
#                     state = "right"
#     print(cnt)

# l = one()
# n_list = list(wow())
# cnt = 0
# for i in n_list:
#     cnt+=1
#     if cnt == i:
#         print(i,end=" ")
#         cnt=0

# l = one()
# n_list = list(wow())
# cnt = 0
# for x in range(l-2):
#     for y in range(x+1,l-1):
#         for z in range(y+1,l):
#             if n_list[x]*n_list[y]==n_list[z]:
#                 cnt+=1
# print(cnt)

# l = one()
# n_list = sorted(list(wow()))
# print(sum(n_list[1:-1]))

# a = inputing().split("()")
# x,y = a
# if len(x) == len(y):
#     print("correct")
# else:
#     print("fix")

# a = sorted(list(wow()))
# b = sorted(list(wow()))
# cnt = 0
# for x,y in zip(a,b):
#     cnt+=x*y
# print(cnt)

# x,n = wow()
# str_str = "1"
# index = 1
# while len(str_str)<n:
#     str_str+=str(x**index)
#     index+=1
# print(str_str[n-1])

# l = one()
# n_list = inputing().split()
# a_list = inputing().split()
# for i in n_list:
#     if i not in a_list:
#         print(i)

# r = one()
# n_list = []
# for _ in range(r):
#     a = inputing().split()
#     a[:3] = map(int,a[:3])
#     n_list.append(a)
# n_list.sort(key=lambda x : (x[0],x[1],x[2]),reverse=True)
# print(*n_list[0][3:])
# left = "qwertasdfgzxcvb"
# right = "yuiophjklnm" 
# a = list(inputing())
# state = "none"
# check = "no"
# for i in a:
#     if state == "none":
#         if i in left:
#             state = "left"
#         else:
#             state = "right"
#     else:
#         if state == "left":
#             if i in left:
#                 check = "yes"
#                 break
#             else:
#                 state = "right"
#         else:
#             if i in right:
#                 check = "yes"
#                 break
#             else:
#                 state = "left"
    
# if check == "yes":
#     print("no")
# else:
#     print("yes")




