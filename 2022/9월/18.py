import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# r,l= wow()
# d_list = [[1,0],[0,1],[-1,0],[0,-1]]
# n_list = [[0]*l for _ in range(r)]
# index = 1
# d_index = 0
# x = 0
# y = 0
# while True:
#     if 0<=x<=l-1 and 0<=y<=r-1:
#         if n_list[y][x] == 0:
#             n_list[y][x]=index
#             x+=d_list[d_index][0]
#             y+=d_list[d_index][1]
#         else:
#             x-=d_list[d_index][0]
#             y-=d_list[d_index][1]
#             index+=1
#             d_index+=1
#             d_index%=4
#             x+=d_list[d_index][0]
#             y+=d_list[d_index][1]
#             if n_list[y][x] != 0:
#                 break
            
#     else:
#         x-=d_list[d_index][0]
#         y-=d_list[d_index][1]
#         index+=1
#         d_index+=1
#         d_index%=4
#         x+=d_list[d_index][0]
#         y+=d_list[d_index][1]
#     # for i in n_list:
#     #     print(*i)
# max_max = 0
# for i in n_list:
#     max_max=max(max_max,max(i))
# print(max_max-1)

# r = one()
# num = one()
# n_list = [[0]*r for _ in range(r)]
# d_list = [[0,1],[1,0],[0,-1],[-1,0]]
# d_index = 0
# x = 0
# y = 0
# index = r*r
# while index != 0:
#     if 0<=x<=r-1 and 0<=y<=r-1:
#         if n_list[y][x] == 0:
#             n_list[y][x]=index
#             index-=1
#             x+=d_list[d_index][0]
#             y+=d_list[d_index][1]
#         else:
#             x-=d_list[d_index][0]
#             y-=d_list[d_index][1]
#             d_index+=1
#             d_index%=4
#             x+=d_list[d_index][0]
#             y+=d_list[d_index][1]
#             if n_list[y][x] !=0:
#                 break
            
#     else:
#         x-=d_list[d_index][0]
#         y-=d_list[d_index][1]
#         d_index+=1
#         d_index%=4
#         x+=d_list[d_index][0]
#         y+=d_list[d_index][1]
# answer = 0
# for y in range(r):
#     for x in range(r):
#         print(n_list[y][x],end=" ")
#         if n_list[y][x] == num:
#             answer = [y+1,x+1]
#     print()
# print(*answer)
            
# n_list = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']
# n = one()
# plus = n//len(n_list)
# for i in range(len(n_list)):
#     if "turu" in n_list[i]:
#         n_list[i]+="ru"*plus
# index = n%len(n_list)-1
# answer = n_list[index] 
# ru = answer.count("ru")       
# if ru >= 5:
#     print(f"tu+ru*{ru}")
# else:
#     print(answer)
# import math
# for _ in range(one()):
#     day = one()
#     n_list = list(wow())
#     gap = math.ceil(len(n_list)/2)
#     index = 1
#     while sum(n_list) <= day:
#         index+=1
#         new_list = []
#         for i in range(len(n_list)):
#             new_list.append(n_list[i]+n_list[i-1]+n_list[i+1 if i+1 < len(n_list) else i+1-len(n_list)]+n_list[(gap+i) if len(n_list) > (gap+i) else (gap+i)-len(n_list)])
#             # print(new_list)
#         n_list = new_list
#     print(index)

# a,b,c= wow()
# x,y,z = wow()
# min_min = min(a/x,b/y,c/z)
# x,y,z = a-min_min*x,b-min_min*y,c-min_min*z
# print(f"{x:.6f} {y:.6f} {z:.6f}")

# r,l = wow()
# n_list = []
# for i in range(r):
#     a = list(wow())
#     for index in range(l):
#         if a[index] == 1:
#             n_list.append([i,index])
# for i in range(0,len(n_list),2):
#     a,b = n_list[i]
#     x,y = n_list[i+1]
#     print(abs(x-a)+abs(y-b))

# n = bin(one())[2:].zfill(32)
# m = bin(int("".join(["1" if i == "0" else "0" for i in n]),2)+1)[2:]
# cnt = 0
# print(m)
# for x,y in zip(n,m):
#     if x != y:
#         cnt+=1
# print(cnt)

# while True:
#     l= one()
#     if l == 0:
#         break
#     n_list = inputing()
#     n_dict = {}
#     state = 0
#     for i in range(0,len(n_list),l):
#         a = n_list[i:i+l]
#         if state == 1:
#             a=a[::-1]
#         for index in range(l):
#             if index not in n_dict:
#                 n_dict[index]=[a[index]]
#             else:
#                 n_dict[index]+=[a[index]]
#         if state == 0:
#             state=1
#         else:
#             state=0
#     for i in range(l):
#         print(*n_dict[i],sep="",end="")
#     print()

# n = inputing()
# str_str = ""
# cnt = 0
# for i in n:
#     if str_str == "":
#         str_str+= i
#     else:
#         if int(str_str[-1])+1 == int(i):
#             str_str+=i
#         else:
#             cnt+=1 if len(str_str) == 3 else 0
#             str_str=i
# cnt+=1 if len(str_str) == 3 else 0
# print(cnt)
         
# a = list(inputing())
# b = inputing()
# state = "none"
# cnt = 1
# for i in b:
#     c = a.index(i) 
#     if state == "none":
#         state = c
#     else:       
#         if c <= state:
#             cnt+=1
#         # print(state,c,cnt)
#         state = c
# print(cnt)

X,Y = wow()
X-=1
Y-=1
n_list = [list(inputing()) for _ in range(10)]
sero_dict = {}
index = 1
for y in range(10):
    if "o" in n_list[y]:
        ind = n_list[y].index("o")
        for yy in range(10):
            n_list[yy][ind]=index
        n_list[y] = [index]*10
    # print(y+1)
    # for i in n_list:
    #     print(*i)
d = 10001
for i in range(10):
    if "x" in n_list[i]:
        for ii in range(10):
            if n_list[i][ii] == "x":
                d = min(d,(abs(X-i)+abs(Y-ii)))
print(d)  











