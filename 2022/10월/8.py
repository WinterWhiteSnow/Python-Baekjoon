import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# https://www.acmicpc.net/problem/25591
# x,y = wow()
# a = 100-x
# b = 100-y
# c = 100-(a+b)
# d = a*b
# q=d//100
# r=d%100
# print(a,b,c,d,q,r)
# print(c+d//100,d%100)

# https://www.acmicpc.net/problem/25600
# max_max = 0
# for _ in range(one()):
#     a,b,c = wow()
#     x = b+c
#     if a == x:
#         cnt = (a*(b+c))*2
#     else:
#         cnt = a*(b+c)
#     max_max=max(max_max,cnt)
# print(max_max)

# https://www.acmicpc.net/problem/25625
# a,b = wow()
# if b <a :
#     print(a+b)
# else:
#     print(b-a)

# https://www.acmicpc.net/problem/25628
# a,b = wow()
# print(min(a//2,b))

#https://www.acmicpc.net/problem/25640
# a = inputing()
# cnt = 0
# for _ in range(one()):
#     b = inputing()
#     if a==b:
#         cnt+=1
# print(cnt)

#https://www.acmicpc.net/problem/25703
# n = one()
# print("int a;")
# for i in range(1,n+1):
#     if i == 1:
#         print("int *ptr = &a;")
#     else:
#         if i == 2:
#             print("int **ptr2 = &ptr;")
#         else:
#             print("int "+"*"*i+f"ptr{i} = &ptr{i-1};")

#https://www.acmicpc.net/problem/25704
# n = one()
# m = one()
# min_min = m
# for i in range(n//5):
#     if i == 0:
#         min_min=min(min_min,m-500)
#     if i == 1:
#         min_min = min(min_min,m*0.9)
#     if i == 2:
#         min_min = min(min_min,m-2000)
#     if i == 3:
#         min_min = min(min_min,m*0.75)
# if min_min < 0:
#     min_min = 0
# print(int(min_min))


                    
                    






