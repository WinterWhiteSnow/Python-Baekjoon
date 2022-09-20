import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# l = one()
# n_list = list(wow())
# print(n_list.index(min(n_list)))

# import math
# a,b = wow()
# n_list = list(wow())
# print(math.ceil((max(n_list)*b)/1000))

# a,b,c = wow()

# index = 0
# cnt = 0
# while cnt<c:
#     index+=1
#     cnt+=a
#     if index%7==0:
#         cnt+=b
# print(index)

# for i in range(one(),1000000001):
#     list_list = list(map(int,list(str(i))))
#     cnt = 0
#     for q in list_list:
#         cnt+=q
#     # print("cnt",cnt)
#     if i%cnt == 0:
#         print(i)
#         exit()

# for _ in range(one()):
#     a,b = inputing().split()
#     print(b*int(a))

# start = inputing()
# cnt = [start]
# for _ in range(one()):
#     win,lose = inputing().split()
#     if win == start:
#         pass
#     if lose == start:
#         start = win
#         cnt.append(start)
# print(start,len(set(cnt)),sep="\n")

# n_list = list(wow())
# cnt = 0
# for i in n_list:
#     if i == 1:
#         cnt+=500
#     if i == 2:
#         cnt+=800
#     if i == 3:
#         cnt+=1000
# print(5000-cnt)

# for _ in range(one()):
#     n,a,b = wow()
#     if a>b:
#         x = a-b
#         y = min(n-b,a)
#     else:
#         x = 0
#         y = min(n-b,a)
#     print(x,y)

# total,h,w = wow()
# print(max(total-h,h)*max(total-w,w)*4)

num = one()
cnt = 0
while num != 1:
    if num%2:
        num+=1
    else:
        num//=2
    cnt+=1
print(cnt)







