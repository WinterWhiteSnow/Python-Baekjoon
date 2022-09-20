import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# 35
# a_list = ["A", "B", "C", "D", "E", "F" ,"G"]
# while True:
#     a = inputing()
#     if a== "#":
#         break
#     a = list(a)
#     check = "ok"
#     for index in range(len(a)-1):
#         x = a_list.index(a[index])
#         y = a_list.index(a[index+1])
#         if x<y:
#             gap = y-x
#         else:
#             gap = 7+y-x
#         if gap%2:
#             check = "no"
#             break
#     if check == "ok":
#         print("That music is beautiful.")
#     else:
#         print("Ouch! That hurts my ears.")

# for _ in range(one()):
#     l = one()
#     a = inputing()
#     if l >= 12:
#         a = list(a)
#         l_check = "no"
#         u_check = "no"
#         symbol_check = "no"
#         n_check = "no"
#         for i in range(l):
#             index = a[i]
#             if index.isdigit():
#                 n_check="yes"
#             if index.isupper():
#                 u_check="yes"
#             if index.islower():
#                 l_check="yes"
#             if index in list("+_)(*&^%$#@!./,;{}"):
#                 symbol_check ="yes"
#         if n_check==l_check==u_check==symbol_check=="yes":
#             print("valid")
#         else:
#             print("invalid")
#     else:
#         print("invalid")

# r = one()
# r_list = set([i for i in range(1,r+1)])
# n_dict = {}
# for _ in range(r):
#     a = one()
#     n_dict[a]=1
# key_list = set(list(n_dict.keys()))
# l = key_list.intersection(r_list)
# print(len(l))

# r,n = wow()
# cnt = 0
# if r>=2:
#     cnt-=n*(r-1)
# for _ in range(r):
#     a,b = inputing().split(":")
#     cnt+=int(a)*60
#     cnt+=int(b)
# h=cnt//3600
# m = (cnt-3600*(cnt//3600))//60
# s = cnt%60
# print(f"{h:0>2}:{m:0>2}:{s:0>2}")

# limit,r = wow()
# cnt = 0
# count = 0
# for _ in range(r):
#     a,b = inputing().split()
#     b = int(b)
#     if a == "enter":
#         if cnt+b<=limit:
#             cnt+=b
#         else:
#             count+=1
#     else:
#         cnt-=b
# print(count)
# a = inputing().split()
# l = len(a)
# cnt = 0
# for i in a:
#     if "ae" in i:
#         cnt+=1
# if cnt/l >= 0.4:
#     print("dae ae ju traeligt va")
# else:
#     print("haer talar vi rikssvenska")

# r = one()
# a_list = []

# for _ in range(r):
#     repeat = one()
#     name = inputing()
#     cnt = 0
#     check_dict = {}
#     for _ in range(repeat):
#         a=inputing()
#         if a == "pea soup":
#             check_dict[a]=1
#         if a == "pancakes":
#             check_dict[a]=1
#     if "pea soup" in check_dict and "pancakes" in check_dict:
#         a_list.append(name)
# if len(a_list) == 0:
#     print("Anywhere is fine I guess")
# else:
#     print(a_list[0])
# n = one()
# if n == 2018:
#     print("yes")
# else:
#     year = 2018
#     month = 4
#     while year<n:
#         year+=2
#         month+=2
#         if month > 12:
#             month-=12
#             year+=1
#     if year == n:
#         print("yes")
#     else:
#         print("no")

# l = one()
# n_list = list(wow())
# n_dict= {}
# for i in range(l-1):
#     n_dict[i+2]=n_list[i]
# list_list = sorted(list(n_dict.items()),key=lambda x : x[1])
# list_list = [a for a,b in list_list]
# print(1,*list_list)

n_list = sorted(list(wow()))
a_list = sorted(list(wow()))
cnt = 0
for x,y in zip(n_list,a_list):
    if x>y:
        cnt+=1
print(cnt)


