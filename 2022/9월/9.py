import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())


# n = one()-1
# x = 0
# y = 0
# for _ in range(n-1):
#     x+=1
#     x%=10
#     y+=1
#     y%=12
# print("ABCDEFGHIJKL"[y-2]+"0123456789"[x-2])

# a,b = wow()
# n_list = [a+b,a-b,a*b]
# max_max = max(n_list)
# if n_list.count(max_max)>=2:
#     print("NIE")
# else:
#     if a < 0:
#         a = "("+str(a)+")"
#     if b < 0:
#         b = "("+str(b)+")"
        
#     if n_list.index(max_max) == 1:
#         if max_max < 0:
#             max_max = "("+str(max_max)+")"
#         print(f"{a}-{b}={max_max}")
#     else:
#         if n_list.index(max_max)==0:
#             if max_max < 0:
#                 max_max = "("+str(max_max)+")"
#             print(f"{a}+{b}={max_max}")
#         else:
#             if max_max < 0:
#                 max_max = "("+str(max_max)+")"
#             print(f"{a}*{b}={max_max}")

# l = one()
# cnt = 0
# state = 0
# first = "none"
# for i in sys.stdin.readline().split():
#     i = int(i)
#     if first == "none":
#         first = i
#     else:
#         state += first-i
#         if state < 0:
#             state = 0
#         cnt = max(cnt,state)
#         first = i
# print(cnt)
# n_list = [list(map(float,inputing().split())) for _ in range(one())]
# for _ in range(one()):
#     l = one()
#     m_list = list(wow())
#     cnt = 0
#     for index in range(1,l):
#         i = m_list[index]
#         x,y = n_list[i]
#         ii = m_list[index-1]
#         a,b = n_list[ii]
#         cnt+=((x-a)**2+(y-b)**2)**(1/2)
#     print(round(cnt))

# l = one()
# n_list = list(wow())
# a,b = inputing().split()
# a = int(a)
# if b == "right":
#     print(sum(n_list[a-1:]),end=" ")
# else:
#     print(sum(n_list[:a]),end=" ")
# a,b = inputing().split()
# a = int(a)
# if b == "right":
#     print(n_list[a-1:].count(0))
# else:
#     print(n_list[:a].count(0))    
# cnt = 0
# for _ in range(one()):
#     a,b = wow()
#     d = (a**2+b**2)**(1/2)
#     if d <10:
#         cnt+=10
#     elif 10<d<=30:
#         cnt+=9
#     elif 30<d<=50:
#         cnt+=8
#     elif 50<d<=70:
#         cnt+=7
#     elif 70<d<=90:
#         cnt+=6
#     elif 90<d<=110:
#         cnt+=5
#     elif 110<d<=130:
#         cnt+=4
#     elif 130<d<=150:
#         cnt+=3
#     elif 150<d<=170:
#         cnt+=2
#     elif 170<d<=190:
#         cnt+=1
#     else:
#         pass
# print(cnt)



