import sys

inputing = lambda : sys.stdin.readline().rstrip()
wow = lambda : map(int,inputing().split())
one = lambda : int(inputing())

# n_dict = {}

# r,l = wow()
# for _ in range(r):
#     a = list(wow())
#     for i in range(1,1+l):
#         if i not in n_dict:
#             n_dict[i]=a[i-1]
#         else:
#             n_dict[i]+=a[i-1]
# list_list = list(n_dict.items())
# list_list.sort(key = lambda x : x[0])
# list_list.sort(key = lambda x : x[1],reverse=True)
# list_list = [a for a,b in list_list]
# print(*list_list)

# r = one()
# r_list = inputing()
# for _ in range(r):
#     str_str = ""
#     new_list = []
#     count = 1
#     now= "none"
#     for index in r_list:
#         if now == "none":
#             now = index
#         else:
#             if now == index:
#                 count+=1
#             else:
#                 str_str+=str(count)+now
#                 now = index
#                 count=1
#     if now != "none":
#         str_str+=str(count)+now
#     r_list=str_str
# print(r_list)

# r = one()
# for _ in range(r):
#     a = inputing()
#     print(a[::-1])
# import math
# total,r = wow()
# for _ in range(r):
#     a,b,c = wow()
#     time = 0
#     cnt = 0
#     while cnt <total:
#         if cnt+a*b < total:
#             time+=b+c
#             cnt+=a*b
#         else:
#             index = math.ceil((total-cnt)/a)
#             cnt+=index
#             time+=index
#             break
#     print(time)
# index=1
# while True:
#     a = one()
#     if a == 0:
#         break
#     a_list = list(wow())
#     average = sum(a_list)//a
#     total = 0
#     for i in a_list:
#         if i >average:
#             total+=i-average
#     print(f"Set #{index}")
#     print(f"The minimum number of moves is {total}.")
#     print()
#     index+=1

# a = one()
# print(f"{a:,}")

# while True:
#     a,b=wow()
#     if a==b==0:
#         break
    
#     n_dict = {}
#     n_list = list(wow())
#     cnt =0
#     for i in n_list:
#         if i not in n_dict:
#             n_dict[i]=1
#         else:
#             n_dict[i]+=1
#     list_list = list(n_dict.values())
#     for i in list_list:
#         if i > 1:
#             cnt+=1
#     print(cnt)

# while True:
#     list_list = inputing()
#     if list_list[0] == "*":
#         break
#     list_list = list_list[1:-1].split("/")
#     count = 0
#     for i in list_list:
#         cnt = 0
#         for index in i:
#             if index == "W":
#                 cnt+=1
#             if index == "H":
#                 cnt+=1/2
#             if index == "Q":
#                 cnt+=1/4
#             if index == "E":
#                 cnt+=1/8
#             if index == "S":
#                 cnt+=1/16
#             if index == "T":
#                 cnt+=1/32
#             if index == "X":
#                 cnt+=1/64
#         if cnt ==1:
#             count+=1
#     print(count)

# while True:
#     a = one()
#     if a == 0:
#         break
#     a_list = [a]
#     while a_list[-1] != 1:
#         if a_list[-1]%2 == 0:
#             a_list.append(a_list[-1]//2)
#         else:
#             a_list.append(3*a_list[-1]+1)
#     print(max(a_list))

for _ in range(one()):
    a,b= inputing().split()
    a = int(a[::-1])
    b = int(b[::-1])
    c = int(str(a+b)[::-1])
    print(c)
        
        
    




            








