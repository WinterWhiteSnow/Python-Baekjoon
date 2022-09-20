import sys


inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# import math
# n = one()
# x = 1
# y = n-x
# for a in range(n//2 if n%2 == 0 else n//2+1,n): #분모
#     for b in range(n-a,n-a+1):#분자
#         if math.gcd(a,b) == 1:
#             if x/y < b/a:
#                 x = b
#                 y = a
# print(x,y)

# a = one()
# total,weight,blue,hair = wow()
# if a== 1: # 최소
#     answer = total*3-(weight+blue+hair)
#     print(0 if total-answer < 0 else total-answer)
# else:#최대
#     print(min(weight,blue,hair))

# a,b = wow()
# index = 1
# start = 10**9
# end = 0
# while True:
#     x = index
#     y = index*2
#     if x<=min(a,b)<=max(a,b)<=y:
#         start = min(start,index)
#         end = max(end,index)
#     else:
#         if max(a,b)<y:
#             break
#     index+=1
# print(start,end)

# now,goal = wow()
# order = inputing()
# if order =="freeze":
#     if now <= goal:
#         print(now)
#     else:
#         print(goal)
# if order == "heat":
#     if now >= goal:
#         print(now)
#     else:
#         print(goal)
# if order == "auto":
#     print(goal)
# if order == "fan":
#     print(now)

# n_dict = {}
# for _ in range(one()):
#     name = inputing()
#     value = one()
#     if value not in n_dict:
#         n_dict[value] = [name]
#     else:
#         n_dict[value]+=[name]
# list_list = list(n_dict.items())
# list_list.sort(key=lambda x : x[0],reverse=True)
# print(list_list[0][1][0])

# r = one()
# n_list = list(wow())
# w_list = list(wow())
# cnt = 0
# for i in range(r):
#     cnt+=w_list[i]*(n_list[i]+n_list[i+1])/2
# print(cnt)

r,l = wow()
n_dict = {}
for _ in range(r):
    name= inputing()
    num_list = inputing()
    n_dict[num_list]=name
list_list = list(n_dict.items())
list_list.sort(key= lambda x : sum(list(map(int,x[0].split()))))
print(list_list[0][1])












