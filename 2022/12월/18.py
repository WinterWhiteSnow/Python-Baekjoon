import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

#https://www.acmicpc.net/problem/1914
# list_list = []
# def hanoi(num,start,goal,temp):
#     if num == 1:
#         print(start,goal)
#         return
#     hanoi(num-1,start,temp,goal)
#     print(start,goal)
#     hanoi(num-1,temp,goal,start)
# n = one()
# print(2**n-1)
# if n <= 20:
    # hanoi(n,1,3,2)

#https://www.acmicpc.net/problem/11729
# def hanoi(num,start,goal,temp):
#     if num == 1:
#         print(start,goal)
#         return
#     hanoi(num-1,start,temp,goal)
#     print(start,goal)
#     hanoi(num-1,temp,goal,start)
# n = one()
# print(2**n-1)
# if n <= 20:
#     hanoi(n,1,3,2)

#Z
# n,x,y = wow()
# cnt = [0]
# def go(n,a,b):
#     if n == 1:
#         return
#     num = n//2
#     x,y = a//num,b//num
#     # print("start",num,x,y)
#     if x==y==0:
#         cnt[0]+=0
#     elif y ==1:
#         if x == 0:
#             cnt[0]+=num**2
#         else:
#             cnt[0]+=(num**2)*3
#     elif x==1 and y ==0:
#         cnt[0]+=(num**2)*2
#     # print(num,a%num,b%num,cnt)
#     go(num,a%num,b%num)
# go(2**n,x,y)
# print(cnt[0])

r = one()
n_list = [list("*"*r) for _ in range(r)]
def go(n,x,y):
    num = n//3
    if num == 0:
        return
    print("Start",num)
    for a in range(num):
        for b in range(num):
            if a==b==1:
                for i in range(num):
                    n_list[y+num*b+i][x+num*a:x+num*a+num]=" "*num
            print(num*a,num*b,a,b)
            go(num,num*a,num*b)
go(r,0,0)
for i in n_list:
    print(*i)    













