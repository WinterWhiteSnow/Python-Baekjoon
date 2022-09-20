import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# a,b = inputing().split()
# a = int(a)
# n_list = [inputing().split() for _ in range(a)]
# index ="none"
# answer = "none"
# ind = 0
# for name,answer in n_list:
#     if b == name:
#         if index == "none":
#             index = ind
#             answer=answer
#             break
#     ind+=1
# new_list = n_list[:index]
# cnt = 0
# for i in new_list:
#     if i[1] == answer:
#         cnt+=1
# print(cnt)

# for _ in range(one()):
#     a,b = inputing().split()
#     if a == "1":
#         b = list(map(int,b.split(".")))
#         str_str = ""
#         for i in b:
#             str_str+=bin(i)[2:].zfill(8)
#         print(int(str_str,2))
#     else:
#         b = bin(int(b))[2:].zfill(64)
#         str_str = ""
#         for i in range(0,len(b),8):
#             str_str+="."+str(int(b[i:i+8],2))
#         print(str_str[1:])

# r = one()
# n_list = [inputing().split() for _ in range(r)]
# for i in range(r):
#     if "5" in n_list[i]:
#         prof_y=n_list[i].index("5")
#         prof_x=i
#     if "2" in n_list[i]:
#         gyu_y=n_list[i].index("2")
#         gyu_x=i
# d = (prof_x-gyu_x)**2+(prof_y-gyu_y)**2
# # print(prof_x,prof_y,gyu_x,gyu_y,d)
# if d>=25:
#     if prof_x==gyu_x:
#         cnt = n_list[prof_x][min(prof_y,gyu_y):max(prof_y,gyu_y)+1].count("1")
#     elif prof_y==gyu_y:
#         cnt = 0
#         for i in range(min(prof_x,gyu_x),max(prof_x,gyu_x)+1):
#             if n_list[i][prof_y] == "1":
#                 cnt+=1
#     else:
#         cnt = 0
#         for x in range(min(prof_x,gyu_x),max(prof_x,gyu_x)+1):
#             for y in range(min(prof_y,gyu_y),max(prof_y,gyu_y)+1):
#                 if n_list[x][y]=="1":
#                     cnt+=1
#     print(1 if cnt >=3 else 0)
# else:
#     print(0)

# l,step = wow()
# n_list = inputing().split()
# str_str = []
# for i in n_list:
#     if len("".join(str_str))+len(i) <= step:
#         str_str.append(i)
#     else:
#         print(*str_str)
#         str_str=[i]
# if len(str_str) != 0:
#     print(*str_str)
# import string
# str_str = list(string.ascii_uppercase)
# n = list(inputing())[::-1]
# index = 0
# cnt = 0
# for i in n:
#     cnt+=(26**index)*(str_str.index(i)+1)
#     index+=1
# print(cnt)

# list_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# time,r = wow()
# cnt = 0
# for _ in range(r):
#     a,b,aa,bb = inputing().split()
#     b,bb = int(b),int(bb)
#     gap = list_list.index(aa)-list_list.index(a)
#     bb+=gap*24
#     cnt+=bb-b
# time = time-cnt
# if time < 0: time=0
# elif time>48:
#     time = -1
# print(time)

# price,remainder = wow()
# n_list = []
# cookie_list = []
# for i in range(9,-1,-1):
#     if remainder >= 2**i:
#         cookie_list.append(2**i)
#         remainder-=2**i
# for i in range(10):
#     n_list.append(2**i)
# n_list.sort(reverse=True)
# cookie_list.sort(reverse=True)
# index = 0
# cnt = 0
# while True:
#     if len(n_list)>index:
#         if cnt+n_list[index] <= price:
#             cnt+=n_list[index]
#             del n_list[index]
#             if len(n_list) == 0:
#                 break
#         else:
#             index+=1
#     else:
#         break
# if price-cnt == 0:
#     print("No thanks")
# else:
#     gap = price-cnt
#     index = 0
#     while True:
#         if len(cookie_list)>index:
#             if cookie_list[index] <= gap:
#                 gap-=cookie_list[index]
#                 del cookie_list[index]
#                 if len(cookie_list)==0:
#                     break
#             else:
#                 index+=1
#         else:
#             break
#         # print(gap,index,cookie_list[index])
#     print("Thanks" if gap == 0 else "Impossible")
        
# total = one()
# gap = 1
# while gap*(gap+1)//2<= total:
#     gap+=1
# if gap%2:
#     print(gap*(gap+1)//2-total)
# else:
#     print(0)

# for _ in range(one()):
#     a = inputing()
#     n_dict = {}
#     for _ in range(one()):
#         b = inputing()
#         cnt = 0
#         for x,y in zip(a,b):
#             if x != y:
#                 cnt+=1
#         n_dict[b]=cnt
#     n_list = sorted(n_dict.items(),key=lambda x : x[1])
#     print(n_list[0][0])

now,l = wow()
n_list = sorted(list(wow()))
if now < 200:
    limit = 200-now
    # print(n_list)
    cnt = 0
    while limit > 0:
        cnt+=1
        limit-=n_list[0]
        del n_list[0]
        if len(n_list) == 0:
            break
    print(cnt)
else:
    print(0)








