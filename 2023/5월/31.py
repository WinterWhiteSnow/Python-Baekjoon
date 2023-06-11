import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1503
# n,m= wow()
# n_list = [i for i in range(1,1002)]
# if m != 0:
#     m_list = list(wow())
#     n_list = [i for i in n_list if i not in m_list]
# min_min = 1000000000000000000000000000000000001
# for x in n_list:
#     for y in n_list:
#         for z in n_list:
#             if abs(n-x*y*z)<min_min:
#                 min_min=abs(n-x*y*z)
# print(min_min)

#https://www.acmicpc.net/problem/1500
# n,k = wow()
# num = n//k
# n_list = [num for _ in range(k)]
# n-=sum(n_list)
# for i in range(n):
#     n_list[i]+=1
# cnt = 1
# for n in n_list:
#     cnt*=n
# print(cnt)

#https://www.acmicpc.net/problem/1564
# cnt = 36288
# n = one()
# for i in range(10,n+1):
#     cnt*=i
#     while cnt>10**5:
#         if cnt%10==0:
#             cnt//=10
#         else:
#             break
#     cnt%=1000000000000
# print(str(cnt)[-5:])

#https://www.acmicpc.net/problem/2072
# def garo(y):
#     cnt = 0
#     state = "none"
#     answer_list = []
#     for x in range(101):
#         if n_list[y][x] != 0:
#             if state == "none":
#                 state = n_list[y][x]
#                 cnt=1
#             else:
#                 if state == n_list[y][x]:
#                     cnt+=1
#                 else:
#                     answer_list.append(cnt)
#                     cnt = 1
#                     state = n_list[y][x]
#         else:
#             answer_list.append(cnt)
#             cnt=0
#             state = "none"
#     answer_list.append(cnt)
#     if 5 in answer_list:
#         return True
#     return False
# def sero(x):
#     cnt = 0
#     state = "none"
#     answer_list = []
#     for y in range(101):
#         if n_list[y][x] != 0:
#             if state == "none":
#                 state = n_list[y][x]
#                 cnt=1
#             else:
#                 if state == n_list[y][x]:
#                     cnt+=1
#                 else:
#                     answer_list.append(cnt)
#                     cnt = 1
#                     state = n_list[y][x]
#         else:
#             answer_list.append(cnt)
#             cnt=0
#             state = "none"
#     answer_list.append(cnt)
#     if 5 in answer_list:
#         return True
#     return False

# def right_diagonal(y,x):
#     while 0<=y-1<101 and 0<=x-1<101:
#         y-=1
#         x-=1
#     cnt = 0
#     state = "none"
#     answer_list = []
#     while 0<=y<101 and 0<=x<101:
#         if n_list[y][x] != 0:
#             if state == "none":
#                 cnt=1
#                 state = n_list[y][x]
#             else:
#                 if state == n_list[y][x]:
#                     cnt+=1
#                 else:
#                     answer_list.append(cnt)
#                     cnt = 1
#                     state = n_list[y][x]
#         else:
#             answer_list.append(cnt)
#             cnt=0
#             state = "none"
#         y+=1
#         x+=1
#     answer_list.append(cnt)
#     # print("answer!")
#     # print(answer_list)
#     if 5 in answer_list:
#         return True
#     return False

# def left_diagonal(y,x):
#     while 0<=y-1<101 and 0<=x+1<101:
#         y-=1
#         x+=1
#     cnt = 0
#     answer_list = []
#     state = "none"
#     while 0<=y<101 and 0<=x<101:
#         if n_list[y][x] != 0:
#             if state == "none":
#                 cnt=1
#                 state = n_list[y][x]
#             else:
#                 if state == n_list[y][x]:
#                     cnt+=1
#                 else:
#                     answer_list.append(cnt)
#                     cnt = 1
#                     state = n_list[y][x]
#         else:
#             answer_list.append(cnt)
#             cnt=0
#             state = "none"                    
#         y+=1
#         x-=1
#     answer_list.append(cnt)
#     if 5 in answer_list:
#         return True
#     return False

                
# r = one()
# a_list = [list(wow()) for _ in range(r)]       
# n_list = [[0]*101 for _ in range(101)]

# for d in range(r):
#     y,x = a_list[d]
#     now =d+1
#     if d%2:
#         symbol = "X"
#     else:
#         symbol = "O"
#     n_list[y][x]=symbol
#     # print(now,symbol)
#     # for i in n_list[:19]:
#     #     print(i[:19])
    
#     a = garo(y)
#     b = sero(x)
#     c = right_diagonal(y,x)
#     d = left_diagonal(y,x)
#     if a or b or c or d:
#         print(now)
#         exit()
# print(-1)

#https://www.acmicpc.net/problem/2725
# import math
# answer_list = [0]
# for y in range(1001):
#     cnt = 0
#     for x in range(y+1):
#         if math.gcd(y,x)==1:
#             if y != x:
#                 cnt+=2
#             else:
#                 cnt+=1
#     answer_list.append(cnt+answer_list[-1])
# for _ in range(one()):
#     print(answer_list[one()+1])

#https://www.acmicpc.net/problem/2777
# for _ in range(one()):
#     num = one()
#     if num == 1:
#         print(1)
#     else:
#         num_list = []
#         for n in range(9,1,-1):
#             while num>=n:
#                 if num%n == 0:
#                     num_list.append(n)
#                     num//=n
#                 else:
#                     break
#         # print(num,num_list)
#         if num>=10:
#             print(-1)
#         else:
#             print(len(num_list))
    
r = one()
down_list = []
time_list = []
for d in range(r):
    s,down = wow()
    for _ in range(down):
        down_list.append(d)
    for _ in range(s):
        time_list.append(d)
print(down_list,len(down_list))
print(time_list,len(time_list))











